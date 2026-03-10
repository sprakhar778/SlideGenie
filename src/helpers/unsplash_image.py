"""
Unsplash API image fetcher.
Uses /search/photos for relevance-ordered results — far more accurate than /photos/random.
"""

import os
import re
import random
import httpx
from dotenv import load_dotenv

load_dotenv()

UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY", "")
UNSPLASH_SEARCH_URL = "https://api.unsplash.com/search/photos"

# Tech/abstract words that cause 403s or zero results on Unsplash
_JARGON = {
    "ai", "ml", "ai-powered", "ai-driven", "ai-enabled", "ai-assisted",
    "ai-analyzed", "ai-generated", "llm", "nlp", "iot", "saas", "blockchain",
    "automated", "algorithmic", "predictive", "generative", "smart",
    "digital", "virtual", "cyber", "tech", "technology", "data-driven",
    "machine-learning", "deep-learning",
}


def _simplify_query(query: str) -> str:
    """Strip jargon/hyphenated tech terms and return a clean short phrase."""
    # Remove hyphenated compound words (e.g. "AI-analyzed" → removed)
    words = re.sub(r'\b\w+-\w+\b', '', query).split()
    # Filter out jargon
    clean = [w for w in words if w.lower().strip(",.") not in _JARGON and len(w) > 2]
    # Return first 3 meaningful words
    return " ".join(clean[:3])


async def fetch_unsplash_image_url(search_query: str) -> str | None:
    """
    Search Unsplash for the most relevant photo using the search endpoint.
    Returns a pre-sized (1280×720, center-cropped) image URL, or None on failure.

    Uses /search/photos (relevance-ordered) and picks randomly from top 10 results
    to get variety while staying relevant.
    """
    if not UNSPLASH_ACCESS_KEY:
        return None

    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                UNSPLASH_SEARCH_URL,
                params={
                    "query": search_query,
                    "orientation": "landscape",
                    "per_page": 10,           # top 10 most relevant results
                    "content_filter": "high", # safe, high-quality only
                    "client_id": UNSPLASH_ACCESS_KEY,
                },
            )
            if response.status_code == 200:
                results = response.json().get("results", [])

                # Fallback: simplify the query if no results or 403
                if not results:
                    simplified = _simplify_query(search_query)
                    if simplified and simplified != search_query:
                        print(f"[Unsplash] No results. Retrying with simplified: '{simplified}'")
                        fb = await client.get(
                            UNSPLASH_SEARCH_URL,
                            params={
                                "query": simplified,
                                "orientation": "landscape",
                                "per_page": 10,
                                "content_filter": "high",
                                "client_id": UNSPLASH_ACCESS_KEY,
                            },
                        )
                        if fb.status_code == 200:
                            results = fb.json().get("results", [])

                if not results:
                    print(f"[Unsplash] No results for: '{search_query}'")
                    return None

                photo = random.choice(results[:10])
                raw_url = photo.get("urls", {}).get("raw")
                if raw_url:
                    return f"{raw_url}&w=1280&h=720&fit=crop&crop=center&q=85&auto=format"
                return None
            else:
                print(f"[Unsplash] API error {response.status_code}")
                return None
    except Exception as e:
        print(f"[Unsplash] Request failed: {e}")
        return None
