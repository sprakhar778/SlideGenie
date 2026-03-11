"""
presentation_management.py – Endpoints for creating, reading, and deleting presentations.

Tags: Presentation Management
"""

import os
import uuid

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from src.api.helpers import (
    initial_state,
    _presentation_path,
    save_presentation,
    load_presentation,
)
from src.api.schemas import (
    PresentationRequest,
    PresentationCreatedResponse,
    PresentationStateResponse,
    PresentationDeletedResponse,
)
from src.helpers.html_to_pdf import generate_presentation_pdf

router = APIRouter(tags=["Presentation Management"])


# -----------------------------------------------
# POST /create-presentation
# -----------------------------------------------

@router.post(
    "/create-presentation",
    response_model=PresentationCreatedResponse,
    summary="Create a new presentation",
    description="Initializes presentation state with user topic and content. Returns a presentation ID used in all subsequent calls.",
)
async def create_presentation(request: PresentationRequest):
    state = initial_state()
    state["topic"] = request.topic
    state["content"] = request.content
    presentation_id = str(uuid.uuid4())
    save_presentation(state, presentation_id)
    return {"message": "Presentation created successfully.", "presentation_id": presentation_id}


# -----------------------------------------------
# GET /presentations/{presentation_id}
# -----------------------------------------------

@router.get(
    "/presentations/{presentation_id}",
    response_model=PresentationStateResponse,
    summary="Get full presentation state",
    description="Returns the complete internal state of the presentation — useful for debugging or resuming a session.",
)
def get_presentation(presentation_id: str):
    state = load_presentation(presentation_id)
    return {"presentation_id": presentation_id, "state": state}


# -----------------------------------------------
# DELETE /presentations/{presentation_id}
# -----------------------------------------------

@router.delete(
    "/presentations/{presentation_id}",
    response_model=PresentationDeletedResponse,
    summary="Delete a presentation",
    description="Permanently deletes the saved presentation JSON file.",
)
def delete_presentation(presentation_id: str):
    output_path = _presentation_path(presentation_id)
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")
    os.remove(output_path)
    return {"message": "Presentation deleted successfully.", "presentation_id": presentation_id}


# -----------------------------------------------
# GET /presentations/{presentation_id}/download
# -----------------------------------------------

@router.get(
    "/presentations/{presentation_id}/download",
    summary="Download presentation as PDF",
    description="Generates a merged PDF of all slides in the presentation and returns it as a file download. Slides that fail to generate will be skipped.",
)
def download_presentation_pdf(presentation_id: str):
    output_path = _presentation_path(presentation_id)
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")
    
    try:
        pdf_path = generate_presentation_pdf(presentation_id)
        if not os.path.exists(pdf_path):
            raise HTTPException(status_code=500, detail="Failed to generate PDF.")
            
        return FileResponse(
            path=pdf_path,
            filename=f"presentation_{presentation_id}.pdf",
            media_type="application/pdf"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating PDF: {str(e)}")
