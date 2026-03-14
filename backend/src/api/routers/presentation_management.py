"""
presentation_management.py – Endpoints for creating, reading, and deleting presentations.

Tags: Presentation Management
"""

import uuid

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from src.api.helpers import (
    initial_state,
    save_presentation,
    load_presentation,
)
from src.api.mongo_db import presentations_collection

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
)
async def create_presentation(request: PresentationRequest):

    state = initial_state()
    state["topic"] = request.topic
    state["content"] = request.content

    presentation_id = str(uuid.uuid4())

    await save_presentation(state, presentation_id)

    return {
        "message": "Presentation created successfully.",
        "presentation_id": presentation_id,
    }


# -----------------------------------------------
# GET /presentations/{presentation_id}
# -----------------------------------------------

@router.get(
    "/presentations/{presentation_id}",
    response_model=PresentationStateResponse,
    summary="Get full presentation state",
)
async def get_presentation(presentation_id: str):

    state = await load_presentation(presentation_id)

    return {
        "presentation_id": presentation_id,
        "state": state,
    }


# -----------------------------------------------
# DELETE /presentations/{presentation_id}
# -----------------------------------------------

@router.delete(
    "/presentations/{presentation_id}",
    response_model=PresentationDeletedResponse,
    summary="Delete a presentation",
)
async def delete_presentation(presentation_id: str):

    result = await presentations_collection.delete_one({"_id": presentation_id})

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Presentation not found",
        )

    return {
        "message": "Presentation deleted successfully.",
        "presentation_id": presentation_id,
    }


# -----------------------------------------------
# GET /presentations/{presentation_id}/download
# -----------------------------------------------
@router.get("/presentations/{presentation_id}/download")
async def download_presentation_pdf(presentation_id: str):

    state = await load_presentation(presentation_id)

    if not state:
        raise HTTPException(status_code=404, detail="Presentation not found")

    try:
        pdf_path = await generate_presentation_pdf(presentation_id, state)

        return FileResponse(
            path=pdf_path,
            filename=f"presentation_{presentation_id}.pdf",
            media_type="application/pdf"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )