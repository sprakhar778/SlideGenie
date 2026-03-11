"""
slide_data_management.py – Endpoints for generating and editing structured slide data.

Tags: Slides Data Management
"""

from fastapi import APIRouter, HTTPException

from src.graph.nodes.slides_data_node import generate_slides_data_node
from src.api.helpers import load_presentation, save_presentation
from src.api.schemas import (
    SlideDataUpdateRequest,
    AllSlidesDataResponse,
    SingleSlideDataResponse,
    SlideDataUpdatedResponse,
)

router = APIRouter(tags=["Slides Data Management"])


# -----------------------------------------------
# GET /presentation-data/{presentation_id}
# -----------------------------------------------

@router.get(
    "/presentation-data/{presentation_id}",
    response_model=AllSlidesDataResponse,
    summary="Generate or get all slides data",
    description="Generates structured slide data (slide_type, content, description) for all slides. Returns existing data if already generated.",
)
def get_presentation_data(presentation_id: str):
    state = load_presentation(presentation_id)
    slides = state.get("slides_data", [])
    if slides and all(s.get("content") for s in slides):
        return {
            "message": "Slides data already generated.",
            "presentation_id": presentation_id,
            "slides_data": slides,
            "total_slides": len(slides),
        }
    updated_state = generate_slides_data_node(state)
    save_presentation(updated_state, presentation_id)
    return {
        "message": "Slides data generated successfully.",
        "presentation_id": presentation_id,
        "slides_data": updated_state["slides_data"],
        "total_slides": len(updated_state["slides_data"]),
    }


# -----------------------------------------------
# GET /presentation-data/{presentation_id}/slide/{slide_index}
# -----------------------------------------------

@router.get(
    "/presentation-data/{presentation_id}/slide/{slide_index}",
    response_model=SingleSlideDataResponse,
    summary="Get a single slide's data",
    description="Returns the slide data (type, content, description) for a specific slide by index.",
)
def get_slide_data(presentation_id: str, slide_index: int):
    state = load_presentation(presentation_id)
    slides = state.get("slides_data", [])
    if slide_index < 0 or slide_index >= len(slides):
        raise HTTPException(
            status_code=404,
            detail=f"Slide index {slide_index} out of range. Total slides: {len(slides)}",
        )
    return {
        "presentation_id": presentation_id,
        "slide_index": slide_index,
        "slide_data": slides[slide_index],
    }


# -----------------------------------------------
# POST /presentation-data/{presentation_id}/slide/{slide_index}
# -----------------------------------------------

@router.post(
    "/presentation-data/{presentation_id}/slide/{slide_index}",
    response_model=SlideDataUpdatedResponse,
    summary="Update a single slide's data",
    description="Manually update the content and/or description of a specific slide by index.",
)
def update_slide_data(presentation_id: str, slide_index: int, request: SlideDataUpdateRequest):
    state = load_presentation(presentation_id)
    slides = state.get("slides_data", [])
    if slide_index < 0 or slide_index >= len(slides):
        raise HTTPException(
            status_code=404,
            detail=f"Slide index {slide_index} out of range. Total slides: {len(slides)}",
        )
    if request.content is not None:
        slides[slide_index]["content"] = request.content
    if request.description is not None:
        slides[slide_index]["description"] = request.description
    state["slides_data"] = slides
    save_presentation(state, presentation_id)
    return {
        "message": "Slide data updated successfully.",
        "presentation_id": presentation_id,
        "slide_index": slide_index,
        "slide_data": slides[slide_index],
    }
