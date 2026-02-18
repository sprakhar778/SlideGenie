# -------------------------------
# Full Pipeline API with CORS fix
# -------------------------------

# ...existing code...

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
import uuid
import os
import logging
logging.basicConfig(level=logging.INFO)

# ---- IMPORT YOUR NODE FUNCTIONS ----
from src.graph.nodes.theme_node import generate_theme_node
from src.graph.nodes.slides_data_node import generate_slides_data_node
from src.graph.nodes.slide_layout_node import generate_slide_layout_node

from src.graph.nodes.slide_generator_node import generate_slides_node


app = FastAPI(title="Presentation Generator API")

# -------------------------------
# CORS Configuration - FIX FOR OPTIONS REQUESTS
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development - restrict in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods including OPTIONS
    allow_headers=["*"],  # Allows all headers
)
def initial_state():
    return {
        "topic": "",
        "content": "",
        "theme_info": "",
        #slide_type,content,description,layout,slide_code
        "slides_data": [],
       
   
    
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)