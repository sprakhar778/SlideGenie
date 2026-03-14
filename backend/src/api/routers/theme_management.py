"""
theme_management.py – Endpoints for generating and updating a presentation theme.

Tags: Theme Management
"""

from fastapi import APIRouter

from src.graph.nodes.theme_node import generate_theme_node
from src.api.helpers import load_presentation, save_presentation
from src.api.schemas import ThemeUpdateRequest, ThemeResponse
from src.helpers.theme_info import get_theme_info
import random   

router = APIRouter(tags=["Theme Management"])

THEMES = [
    "Obsidian Pro",
    "Midnight Galaxy",
    "Aurora Dark",
    "Ember Slate",
    "Forest Executive",
    "Ocean Depths",
    "Solar Flare",
    "Neon Cyberpunk",
    "Tropical Punch",
    "Crimson Noir",
    "Slate Steel",
    "Glacier Light",
    "Arctic Frost",
    "Modern Minimalist",
    "Rose Quartz",
]

# -----------------------------------------------
# GET /presentation-theme/{presentation_id}
# -----------------------------------------------

@router.get(
    "/presentation-theme/{presentation_id}",
    response_model=ThemeResponse,
    summary="Generate or get theme",
    description="Generates a presentation theme based on topic and content. Returns the existing theme if already generated.",
)
def get_presentation_theme(presentation_id: str, theme_name: str = None):
    if theme_name:
        state = load_presentation(presentation_id)
        state["theme_name"] = theme_name    
        state["theme_info"] = get_theme_info(theme_name)
        save_presentation(state, presentation_id)
        return {
            "message": "Theme updated successfully.",
            "presentation_id": presentation_id,
            "theme_info": state["theme_info"],
            "theme_name":state.get("theme_name",""),
        }
        
    state = load_presentation(presentation_id)
    
    #if already theme is generated then return that theme by ai and ask again give random theme
    if state.get("theme_info"):
        theme_name=random.choice(THEMES)
        state["theme_name"] = theme_name    
        state["theme_info"] = get_theme_info(theme_name)
        save_presentation(state, presentation_id)
        return {
            "message": "Theme already generated.",
            "presentation_id": presentation_id,
            "theme_info": state["theme_info"],
            "theme_name":state.get("theme_name",""),
        }
    updated_state = generate_theme_node(state)
    await save_presentation(updated_state, presentation_id)
    return {
        "message": "Theme generated successfully.",
        "presentation_id": presentation_id,
        "theme_info": updated_state["theme_info"],
        "theme_name":updated_state["theme_name"]
       
    }


# -----------------------------------------------
# POST /presentation-theme/{presentation_id}
# -----------------------------------------------

@router.post(
    "/presentation-theme/{presentation_id}",
    response_model=ThemeResponse,
    summary="Update theme",
    description="Manually overrides the theme information for a presentation.",
)
async def update_presentation_theme(presentation_id: str, request: ThemeUpdateRequest):
    state = await load_presentation(presentation_id)
    state["theme_info"] = request.theme_info
    await save_presentation(state, presentation_id)
    return {
        "message": "Theme updated successfully.",
        "presentation_id": presentation_id,
        "theme_info": state["theme_info"],
        "theme_name":state.get("theme_name",""),
        
    }
