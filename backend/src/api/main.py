# -------------------------------
# SlideGenie API – App Factory
# -------------------------------
# All endpoints live in their respective router files under src/api/routers/.
# This file only wires up the app, middleware, and routers.

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api.helpers import start_browser, stop_browser,get_browser

from src.api.routers import (
    presentation_management,
    theme_management,
    slide_data_management,
    slide_layout_management,
    slide_code,
    utility,
)

logging.basicConfig(level=logging.INFO)

# -----------------------------------------------
# App
# -----------------------------------------------

app = FastAPI(
    title="SlideGenie API",
    description="Presentation generation pipeline API",
)

# -----------------------------------------------
# CORS
# -----------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await start_browser()


# -----------------------------------------------
# Routers
# -----------------------------------------------

app.include_router(presentation_management.router)
app.include_router(theme_management.router)
app.include_router(slide_data_management.router)
app.include_router(slide_layout_management.router)
app.include_router(slide_code.router)
app.include_router(utility.router)


# -----------------------------------------------
# Entry point
# -----------------------------------------------


@app.on_event("shutdown")
async def shutdown():
    await stop_browser()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)

# python -m src.api.main