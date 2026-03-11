"""
utility.py – Health-check and miscellaneous utility endpoints.

Tags: Utility
"""

from fastapi import APIRouter
from src.api.schemas import HealthCheckResponse

router = APIRouter(tags=["Utility"])


# -----------------------------------------------
# GET /health
# -----------------------------------------------

@router.get(
    "/health",
    response_model=HealthCheckResponse,
    summary="Health check",
    description="Returns service health status.",
)
def health_check():
    return {"status": "ok"}