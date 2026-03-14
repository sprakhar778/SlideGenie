"""
slide_layout_management.py – Endpoints for assigning and regenerating slide layouts.

Tags: Slide Layout Management
"""

from fastapi import APIRouter, HTTPException

from src.graph.nodes.slide_layout_node import generate_slide_layout_node
from src.helpers.get_layout import get_layout
from src.api.helpers import load_presentation, save_presentation
from src.api.schemas import (
    AllSlidesLayoutResponse,
    SingleSlideLayoutResponse,
    SlideLayoutRegeneratedResponse,
)

router = APIRouter(tags=["Slide Layout Management"])


# -----------------------------------------------
# GET /presentation-layout/{presentation_id}
# -----------------------------------------------

@router.get(
    "/presentation-layout/{presentation_id}",
    response_model=AllSlidesLayoutResponse,
    summary="Generate or get layout for all slides",
    description="Assigns a layout template to every slide based on its slide_type. Returns existing layouts if already assigned.",
)
async def get_presentation_layout(presentation_id: str):
    state = await load_presentation(presentation_id)
    slides = state.get("slides_data", [])
    if slides and all(s.get("layout") for s in slides):
        return {
            "message": "Slide layouts already generated.",
            "presentation_id": presentation_id,
            "slides_data": slides,
        }
    updated_state = generate_slide_layout_node(state)
    await save_presentation(updated_state, presentation_id)
    return {
        "message": "Slide layouts generated successfully.",
        "presentation_id": presentation_id,
        "slides_data": updated_state["slides_data"],
    }


# -----------------------------------------------
# GET /presentation-layout/{presentation_id}/slide/{slide_index}
# -----------------------------------------------

@router.get(
    "/presentation-layout/{presentation_id}/slide/{slide_index}",
    response_model=SingleSlideLayoutResponse,
    summary="Get layout for a single slide",
    description="Returns the assigned layout for a specific slide by index.",
)
async def get_slide_layout(presentation_id: str, slide_index: int):
    state = await load_presentation(presentation_id)
    slides = state.get("slides_data", [])
    if slide_index < 0 or slide_index >= len(slides):
        raise HTTPException(
            status_code=404,
            detail=f"Slide index {slide_index} out of range. Total slides: {len(slides)}",
        )
    slide = slides[slide_index]
    if not slide.get("layout"):
        raise HTTPException(
            status_code=404,
            detail="Layout not yet generated for this slide. Call GET /presentation-layout/{id} first.",
        )
    return {
        "presentation_id": presentation_id,
        "slide_index": slide_index,
        "layout": slide["layout"],
        "slide_data": slide,
    }


# -----------------------------------------------
# POST /presentation-layout/{presentation_id}/slide/{slide_index}/regenerate
# -----------------------------------------------

@router.post(
    "/presentation-layout/{presentation_id}/slide/{slide_index}/regenerate",
    response_model=SlideLayoutRegeneratedResponse,
    summary="Regenerate layout for a single slide",
    description="Force-regenerates the layout for a specific slide. Useful when slide content has been manually updated.",
)
async def regenerate_slide_layout(presentation_id: str, slide_index: int):
    state = await load_presentation(presentation_id)
    slides = state.get("slides_data", [])
    if slide_index < 0 or slide_index >= len(slides):
        raise HTTPException(
            status_code=404,
            detail=f"Slide index {slide_index} out of range. Total slides: {len(slides)}",
        )
    slide = slides[slide_index]
    slide["layout"] = get_layout(slide["slide_type"])
    slides[slide_index] = slide
    state["slides_data"] = slides
    await save_presentation(state, presentation_id)
    return {
        "message": "Slide layout regenerated successfully.",
        "presentation_id": presentation_id,
        "slide_index": slide_index,
        "layout": slide["layout"],
    }
