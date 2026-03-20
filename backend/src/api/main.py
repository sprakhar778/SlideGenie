# -------------------------------
# SlideGenie API – App Factory
# -------------------------------
# All endpoints live in their respective router files under src/api/routers/.
# This file only wires up the app, middleware, and routers.

import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.api.helpers import start_browser, stop_browser
from src.api.routers import (
    presentation_management,
    theme_management,
    slide_data_management,
    slide_layout_management,
    slide_code,
    utility,
)

logging.basicConfig(level=logging.INFO)




@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await start_browser()
    yield
    # Shutdown
    await stop_browser()

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


        
# -----------------------------------------------
# Entry point
# -----------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)

# python -m src.api.main