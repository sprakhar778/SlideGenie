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
import json

async def clean_html_stream(gemini_stream):
    """Intercepts chunks from Gemini and removes Markdown backticks on the fly."""
    
    async for chunk in gemini_stream:
        # Extract the text from the Gemini chunk
        text = chunk.content if hasattr(chunk, "content") else str(chunk)
        if not text:
            continue
            
        # Strip out the opening and closing markdown tags.
        # This handles the tags no matter which chunk they appear in.
        cleaned_chunk = text.replace("```html\n", "").replace("```html", "").replace("```", "")
        
        # Only yield if there's still text left after cleaning
        if cleaned_chunk:
            yield cleaned_chunk

def save_presentation(state, presentation_id):
    output_dir = "generated_presentations"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{presentation_id}.json")
    temp_path = output_path + ".tmp"

    # Write to temp file first
    with open(temp_path, "w") as f:
        json.dump(state, f, indent=4)

    # Atomically replace
    os.replace(temp_path, output_path)

def load_presentation(presentation_id):
    output_path = os.path.join("generated_presentations", f"{presentation_id}.json")

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
            detail="Presentation state corrupted. Please recreate."
        )
    

class PresentationRequest(BaseModel):
    topic: str
    content: str

@app.post("/create-presentation")
async def create_presentation(request:PresentationRequest):
    # Step 1: Initialize state with user input
    state = initial_state()
    state["topic"] = request.topic
    state["content"] = request.content
    
    # Save initial state
    presentation_id = str(uuid.uuid4())
    save_presentation(state, presentation_id)
    
    return {"message": "Presentation created successfully.", "presentation_id": presentation_id}
    

@app.get("/presentation-theme/{presentation_id}")
def get_presentation_theme(presentation_id: str):
    # Load the presentation state
    output_path = os.path.join("generated_presentations", f"{presentation_id}.json")
    
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")
    
    state = load_presentation(presentation_id)
    if state.get("theme_info"):
        return {"message": "Theme already generated.", "presentation_id": presentation_id, "theme_info": state["theme_info"]}
    
    # Step 2: Generate theme
    updated_state = generate_theme_node(state)
    
    # Save updated state
    save_presentation(updated_state, presentation_id)
    
    return {"message": "Theme generated successfully.", "presentation_id": presentation_id,"theme_info": updated_state["theme_info"]}

@app.post("/presentation-theme/{presentation_id}")
def update_presentation_theme(presentation_id: str, request:str):
    # Load the presentation state
    output_path = os.path.join("generated_presentations", f"{presentation_id}.json")
    
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")
    
    state = load_presentation(presentation_id)
    
    # Update theme info in state
    state["theme_info"] = request
    
    # Save updated state
    save_presentation(state, presentation_id)
    
    return {"message": "Theme updated successfully.", "presentation_id": presentation_id, "theme_info": state["theme_info"]}

@app.get("/presentation-layout/{presentation_id}")
def get_presentation_layout(presentation_id: str,presentation_index:int=0):
    # Load the presentation state
    output_path = os.path.join("generated_presentations", f"{presentation_id}.json")
    
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")

    
    state = load_presentation(presentation_id)

    if state.get("slides_data")[presentation_index].get("layout"):
        return {"message": "Slide layout already generated.", "presentation_id": presentation_id, "slides_data": state["slides_data"]}
 
    # Step 3: Generate slide layout
    updated_state = generate_slide_layout_node(state)
    
    # Save updated state
    save_presentation(updated_state, presentation_id)
    
    return {"message": "Slide layout generated successfully.", "presentation_id": presentation_id, "slides_data": updated_state["slides_data"]}
   
@app.get("/presentation-data/{presentation_id}")
def get_presentation_data(presentation_id: str):
    # Load the presentation state
    output_path = os.path.join("generated_presentations", f"{presentation_id}.json")
    
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")
    
    state = load_presentation(presentation_id)

    if state.get("slides_data").get("content"):
        return {"message": "Slides data already generated.", "presentation_id": presentation_id, "slides_data": state["slides_data"]}
    
    # Step 4: Generate slides data
    updated_state = generate_slides_data_node(state)
    
    # Save updated state
    save_presentation(updated_state, presentation_id)
    
    return {"message": "Slides data generated successfully.", "presentation_id": presentation_id, "slides_data": updated_state["slides_data"]}

from fastapi.responses import StreamingResponse
import json

@app.get("/presentation-slides/{presentation_id}")
async def get_presentation_slides(presentation_id: str):

    if not os.path.exists(os.path.join("generated_presentations", f"{presentation_id}.json")):
        raise HTTPException(status_code=404, detail="Presentation not found.")

    state = load_presentation(presentation_id)

    slide_stream = generate_slides_node(state)   # ❗ no await
    cleaned_stream = clean_html_stream(slide_stream)

    return StreamingResponse(cleaned_stream, media_type="text/html")

#test curl -N http://localhost:8000/presentation-slides/presentation_id

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)


# python -m src.api.main