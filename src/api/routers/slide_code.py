"""
slide_code.py – Streaming endpoint for generating slide HTML code.

Tags: Slide Code Generation
"""

import json
import os

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse

from src.graph.nodes.slide_generator_node import generate_slides_node
from src.api.helpers import load_presentation, save_presentation, _presentation_path

router = APIRouter(tags=["Slide Code Generation"])


# -----------------------------------------------
# Stream helper
# -----------------------------------------------

async def clean_html_stream_and_save(gemini_stream, presentation_id: str, state: dict):
    """Strips markdown fences, preserves slide structure as NDJSON, and saves final HTML."""
    slide_html_accumulator = {}
    
    async for chunk in gemini_stream:
        if not isinstance(chunk, dict):
            continue
        slide_index = chunk.get("slide_index")
        token = chunk.get("token", "")
        
        if slide_index is not None and slide_index not in slide_html_accumulator:
            slide_html_accumulator[slide_index] = []
            
        if not token:
            if "done" in chunk:
                # Save the accumulated HTML to the state once a slide finishes
                if slide_index is not None:
                    final_html = "".join(slide_html_accumulator[slide_index])
                    slides = state.get("slides_data", [])
                    if 0 <= slide_index < len(slides):
                        slides[slide_index]["slide_code"] = final_html
                        save_presentation(state, presentation_id)
                yield json.dumps({"slide_index": slide_index, "done": True}) + "\n"
            continue
            
        cleaned_token = (
            token
            .replace("```html\n", "")
            .replace("```html", "")
            .replace("```", "")
        )
        if cleaned_token:
            if slide_index is not None:
                slide_html_accumulator[slide_index].append(cleaned_token)
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
        "Uses up to 2 concurrent LLM calls. Saves the final generated HTML back to the presentation state."
    ),
)
async def get_presentation_slides(presentation_id: str):
    if not os.path.exists(_presentation_path(presentation_id)):
        raise HTTPException(status_code=404, detail="Presentation not found.")
    state = load_presentation(presentation_id)
    slide_stream = generate_slides_node(state)
    cleaned_stream = clean_html_stream_and_save(slide_stream, presentation_id, state)
    
    return StreamingResponse(cleaned_stream, media_type="application/x-ndjson")

