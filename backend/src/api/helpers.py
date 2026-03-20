"""
helpers.py – Shared state helpers used across all routers.

Functions here are intentionally kept pure (file I/O only) so each
router can import them without circular dependency issues.
"""

import json
import os
from datetime import datetime

from fastapi import HTTPException
from src.api.mongo_db import presentations_collection
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
        "created_at": datetime.utcnow().isoformat(),
    }


def _presentation_path(presentation_id: str) -> str:
    return os.path.join(PRESENTATIONS_DIR, f"{presentation_id}.json")


def _presentation_path_pdf(presentation_id: str) -> str:
    return os.path.join(PRESENTATIONS_DIR, f"{presentation_id}.pdf")



     



# -----------------------------------------------
# MongoDB helpers
# -----------------------------------------------

async def save_presentation(state: dict, presentation_id: str) -> None:
    """Save or update presentation in MongoDB"""

    try:
        await presentations_collection.update_one(
            {"_id": presentation_id},
            {"$set": {"state": state}},
            upsert=True,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to save presentation: {str(e)}",
        )



local_cache={}

async def load_presentation(presentation_id: str) -> dict:
    """Load presentation from MongoDB"""

    try:
        if presentation_id in local_cache:
            return local_cache[presentation_id]
            
        presentation = await presentations_collection.find_one(
            {"_id": presentation_id}
        )

        if not presentation:
          raise HTTPException(
            status_code=404,
            detail="Presentation not found",
        )

        local_cache[presentation_id] = presentation["state"]
        return presentation["state"]

   

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to load presentation: {str(e)}",
        )


#----------------------------------------
# Playwright helpers
#----------------------------------------
from playwright.async_api import async_playwright

playwright_instance = None
browser = None


async def start_browser():
    global playwright_instance, browser

    playwright_instance = await async_playwright().start()

    browser = await playwright_instance.chromium.launch(
        headless=True,
        args=["--disable-dev-shm-usage"]
    )

    print("✓ Playwright browser started")


async def stop_browser():
    global playwright_instance, browser

    if browser:
        await browser.close()

    if playwright_instance:
        await playwright_instance.stop()

    print("✓ Playwright browser closed")


def get_browser():
    if browser is None:
        raise RuntimeError("Browser not started")

    return browser