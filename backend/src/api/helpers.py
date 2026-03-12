"""
helpers.py – Shared state helpers used across all routers.

Functions here are intentionally kept pure (file I/O only) so each
router can import them without circular dependency issues.
"""

import json
import os

from fastapi import HTTPException

# -----------------------------------------------
# Constants
# -----------------------------------------------
PRESENTATIONS_DIR = "generated_presentations"


# -----------------------------------------------
# State helpers
# -----------------------------------------------

def initial_state() -> dict:
    """Return a blank presentation state dict."""
    return {
        "topic": "",
        "content": "",
        "theme_info": "",
        # Each slide: { slide_type, content, description, layout, slide_code }
        "slides_data": [],
    }


def _presentation_path(presentation_id: str) -> str:
    return os.path.join(PRESENTATIONS_DIR, f"{presentation_id}.json")


def save_presentation(state: dict, presentation_id: str) -> None:
    """Atomically write presentation state to disk."""
    os.makedirs(PRESENTATIONS_DIR, exist_ok=True)
    output_path = _presentation_path(presentation_id)
    temp_path = output_path + ".tmp"
    with open(temp_path, "w") as f:
        json.dump(state, f, indent=4)
    os.replace(temp_path, output_path)


def load_presentation(presentation_id: str) -> dict:
    """Load presentation state from disk. Raises 404/500 on failure."""
    output_path = _presentation_path(presentation_id)
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")
    try:
        with open(output_path, "r") as f:
            content = f.read().strip()
            if not content:
                raise ValueError("Empty file")
            return json.loads(content)
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Presentation state corrupted. Please recreate.",
        )


