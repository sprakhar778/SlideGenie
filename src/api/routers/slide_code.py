"""
slide_code.py – Streaming endpoint for generating slide HTML code.

Tags: Slide Code Generation
"""

import json
import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from src.graph.nodes.slide_generator_node import generate_slides_node
from src.api.helpers import load_presentation, _presentation_path

router = APIRouter(tags=["Slide Code Generation"])


# -----------------------------------------------
# Stream helper
# -----------------------------------------------

async def clean_html_stream(gemini_stream):
    """Strips markdown fences, preserves slide structure as NDJSON."""
    async for chunk in gemini_stream:
        if not isinstance(chunk, dict):
            continue
        slide_index = chunk.get("slide_index")
        token = chunk.get("token", "")
        if not token:
            if "done" in chunk:
                yield json.dumps({"slide_index": slide_index, "done": True}) + "\n"
            continue
        cleaned_token = (
            token
            .replace("```html\n", "")
            .replace("```html", "")
            .replace("```", "")
        )
        if cleaned_token:
            yield json.dumps({"slide_index": slide_index, "token": cleaned_token}) + "\n"


# -----------------------------------------------
# GET /presentation-slides/{presentation_id}
# -----------------------------------------------

@router.get(
    "/presentation-slides/{presentation_id}",
    summary="Stream slide HTML for all slides",
    description=(
        "Streams HTML code for each slide as NDJSON (newline-delimited JSON). "
        "Each line is a JSON object: `{slide_index: int, token: str}` or `{slide_index: int, done: true}`. "
        "Uses up to 2 concurrent LLM calls."
    ),
)
async def get_presentation_slides(presentation_id: str):
    if not os.path.exists(_presentation_path(presentation_id)):
        raise HTTPException(status_code=404, detail="Presentation not found.")
    state = load_presentation(presentation_id)
    slide_stream = generate_slides_node(state)
    cleaned_stream = clean_html_stream(slide_stream)
    return StreamingResponse(cleaned_stream, media_type="application/x-ndjson")
