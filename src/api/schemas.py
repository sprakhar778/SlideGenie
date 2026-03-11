"""
schemas.py – Pydantic request and response models for the SlideGenie API.

All models are grouped by feature area to match the router tags used in main.py.
Import from here in routers and main.py so the contract is defined in one place.
"""

from typing import Any, Optional
from pydantic import BaseModel, Field


# ============================================================
# ── Presentation Management ──────────────────────────────────
# ============================================================

# ── Requests ─────────────────────────────────────────────────

class PresentationRequest(BaseModel):
    """Body for POST /create-presentation"""
    topic: str = Field(..., description="The main topic / title of the presentation.")
    content: str = Field(..., description="Raw body content or notes to build the presentation from.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "topic": "Introduction to Quantum Computing",
                "content": "Quantum computing uses quantum-mechanical phenomena such as superposition and entanglement..."
            }
        }
    }


# ── Responses ────────────────────────────────────────────────

class PresentationCreatedResponse(BaseModel):
    """Response for POST /create-presentation"""
    message: str
    presentation_id: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "message": "Presentation created successfully.",
                "presentation_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }
        }
    }


class PresentationStateResponse(BaseModel):
    """Response for GET /presentations/{presentation_id}"""
    presentation_id: str
    state: dict[str, Any] = Field(..., description="Full internal presentation state.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "presentation_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "state": {
                    "topic": "Quantum Computing",
                    "content": "...",
                    "theme_info": "",
                    "slides_data": []
                }
            }
        }
    }


class PresentationDeletedResponse(BaseModel):
    """Response for DELETE /presentations/{presentation_id}"""
    message: str
    presentation_id: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "message": "Presentation deleted successfully.",
                "presentation_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }
        }
    }


# ============================================================
# ── Theme Management ─────────────────────────────────────────
# ============================================================

# ── Requests ─────────────────────────────────────────────────

class ThemeUpdateRequest(BaseModel):
    """Body for POST /presentation-theme/{presentation_id}"""
    theme_info: str = Field(
        ...,
        description="Manually supplied theme descriptor (colors, fonts, style) to override the LLM-generated theme."
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "theme_info": "Dark tech theme: background #0d1117, accent #58a6ff, font Inter, minimal icons."
            }
        }
    }


# ── Responses ────────────────────────────────────────────────

class ThemeResponse(BaseModel):
    """Response for GET and POST /presentation-theme/{presentation_id}"""
    message: str
    presentation_id: str
    theme_info: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "message": "Theme generated successfully.",
                "presentation_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "theme_info": "Dark tech theme: background #0d1117, accent #58a6ff, font Inter."
            }
        }
    }


# ============================================================
# ── Slides Data Management ───────────────────────────────────
# ============================================================

# ── Shared inner model ───────────────────────────────────────

# class SlideData(BaseModel):
#     """Shape of a single slide's structured data."""
#     slide_type: Optional[str] = Field(None, description="Category / type of the slide (e.g. 'title', 'bullets', 'image').")
#     content: Optional[str] = Field(None, description="Body content of the slide.")
#     description: Optional[str] = Field(None, description="Visual/layout description hint for this slide.")
#     layout: Optional[str] = Field(None, description="Layout template name assigned to this slide.")
#     slide_code: Optional[str] = Field(None, description="Final rendered HTML code for this slide.")


# ── Requests ─────────────────────────────────────────────────

class SlideDataUpdateRequest(BaseModel):
    """Body for POST /presentation-data/{presentation_id}/slide/{slide_index}"""
    content: Optional[str] = Field(None, description="Updated slide content.")
    description: Optional[str] = Field(None, description="Updated visual description for the slide.")

    model_config = {
        "json_schema_extra": {
            "example": {
                "content": "Quantum bits, or qubits, can exist in superposition of 0 and 1 simultaneously.",
                "description": "Minimalist diagram slide with a single central graphic."
            }
        }
    }


# ── Responses ────────────────────────────────────────────────

class AllSlidesDataResponse(BaseModel):
    """Response for GET /presentation-data/{presentation_id}"""
    message: str
    presentation_id: str
    slides_data: list[SlideData]
    total_slides: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "message": "Slides data generated successfully.",
                "presentation_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "slides_data": [
                    {"slide_type": "title", "content": "Quantum Computing", "description": "Hero title slide", "layout": None, "slide_code": None}
                ],
                "total_slides": 1
            }
        }
    }


class SingleSlideDataResponse(BaseModel):
    """Response for GET /presentation-data/{presentation_id}/slide/{slide_index}"""
    presentation_id: str
    slide_index: int
    slide_data: SlideData


class SlideDataUpdatedResponse(BaseModel):
    """Response for POST /presentation-data/{presentation_id}/slide/{slide_index}"""
    message: str
    presentation_id: str
    slide_index: int
    slide_data: SlideData

    model_config = {
        "json_schema_extra": {
            "example": {
                "message": "Slide data updated successfully.",
                "presentation_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "slide_index": 2,
                "slide_data": {
                    "slide_type": "bullets",
                    "content": "Updated content here.",
                    "description": "Updated description.",
                    "layout": "two-column",
                    "slide_code": None
                }
            }
        }
    }


# ============================================================
# ── Slide Layout Management ──────────────────────────────────
# ============================================================

# ── Responses ────────────────────────────────────────────────

class AllSlidesLayoutResponse(BaseModel):
    """Response for GET /presentation-layout/{presentation_id}"""
    message: str
    presentation_id: str
    slides_data: list[SlideData]

    model_config = {
        "json_schema_extra": {
            "example": {
                "message": "Slide layouts generated successfully.",
                "presentation_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "slides_data": []
            }
        }
    }


class SingleSlideLayoutResponse(BaseModel):
    """Response for GET /presentation-layout/{presentation_id}/slide/{slide_index}"""
    presentation_id: str
    slide_index: int
    layout: str
    slide_data: SlideData


class SlideLayoutRegeneratedResponse(BaseModel):
    """Response for POST /presentation-layout/{presentation_id}/slide/{slide_index}/regenerate"""
    message: str
    presentation_id: str
    slide_index: int
    layout: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "message": "Slide layout regenerated successfully.",
                "presentation_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "slide_index": 1,
                "layout": "bullets-left"
            }
        }
    }


# ============================================================
# ── Slide Code Generation (Streaming) ────────────────────────
# ============================================================
# The /presentation-slides/{presentation_id} endpoint streams
# The two token
# shapes are documented here for reference:

# class SlideStreamToken(BaseModel):
#     """One NDJSON chunk emitted during streaming (partial HTML token)."""
#     slide_index: int
#     token: str


# class SlideStreamDone(BaseModel):
#     """One NDJSON chunk emitted when a slide finishes streaming."""
#     slide_index: int
#     done: bool = True


# ============================================================
# ── Utility ──────────────────────────────────────────────────
# ============================================================

class HealthCheckResponse(BaseModel):
    """Response for GET /health"""
    status: str

    model_config = {
        "json_schema_extra": {
            "example": {"status": "ok"}
        }
    }
