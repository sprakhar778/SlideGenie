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
from fastapi.responses import StreamingResponse
import json

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
    """Cleans markdown but preserves slide structure."""

    async for chunk in gemini_stream:

        # Expecting structured chunk like:
        # { "slide_index": 0, "token": "```html" }

        if not isinstance(chunk, dict):
            continue

        slide_index = chunk.get("slide_index")
        token = chunk.get("token", "")

        if not token:
            continue

        # Remove markdown
        cleaned_token = (
            token
            .replace("```html\n", "")
            .replace("```html", "")
            .replace("```", "")
        )

        if cleaned_token:

            yield json.dumps({
                "slide_index": slide_index,
                "token": cleaned_token
            }) + "\n"

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



#-------------------------------create presentation endpoint - initializes state and saves it----------------------------------
@app.post("/create-presentation",description="Initializes presentation state with user input and saves it. Returns presentation ID for further processing.",tags=["Presentation Management"])
async def create_presentation(request:PresentationRequest):
    # Step 1: Initialize state with user input
    state = initial_state()
    state["topic"] = request.topic
    state["content"] = request.content
    
    # Save initial state
    presentation_id = str(uuid.uuid4())
    save_presentation(state, presentation_id)
    
    return {"message": "Presentation created successfully.", "presentation_id": presentation_id}
    
#-------------------------------get presentation theme - generates theme if not already generated, otherwise returns existing theme----------------------------------
@app.get("/presentation-theme/{presentation_id}",description="Generates presentation theme based on topic and content if not already generated. Returns existing theme if already generated.",tags=["Theme Management"])
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


#-------------------------------update presentation theme - allows updating theme info in state-------------------------------
@app.post("/presentation-theme/{presentation_id}",description="Updates the theme information for a presentation. Accepts new theme info in the request body and updates the presentation state accordingly.",tags=["Theme Management"])
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


#-------------------------------get presentation slides data - generates slides data if not already generated, otherwise returns existing slides data
@app.get("/presentation-data/{presentation_id}",description="Generates slides data for the presentation based on topic and content if not already generated. Returns existing slides data if already generated.",tags=["Slides Data Management"])
def get_presentation_data(presentation_id: str, presentation_index: int = 0):
    # Load the presentation state
    output_path = os.path.join("generated_presentations", f"{presentation_id}.json")
    
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")
    
    state = load_presentation(presentation_id)

    if state.get("slides_data")[presentation_index].get("content"):
        return {"message": "Slides data already generated.", "presentation_id": presentation_id, "slides_data": state["slides_data"][presentation_index]}
    
    # Step 4: Generate slides data
    updated_state = generate_slides_data_node(state)
    
    # Save updated state
    save_presentation(updated_state, presentation_id)
    
    return {"message": "Slides data generated successfully.", "presentation_id": presentation_id, "slides_data": updated_state["slides_data"][presentation_index]}


#-------------------------------get presentation slide layout - generates slide layout if not already generated, otherwise returns existing slide layout-------------
@app.get("/presentation-layout/{presentation_id}",description="Generates slide layout for each slide based on the presentation state if not already generated. Returns existing slide layout if already generated.",tags=["Slide Layout Management"])
def get_presentation_layout(presentation_id: str,presentation_index:int=0):
    # Load the presentation state
    output_path = os.path.join("generated_presentations", f"{presentation_id}.json")
    
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")

    
    state = load_presentation(presentation_id)

    if state.get("slides_data")[presentation_index].get("layout"):
        return {"message": "Slide layout already generated.", "presentation_id": presentation_id, "slides_data": state["slides_data"][presentation_index]}
 
    # Step 3: Generate slide layout
    updated_state = generate_slide_layout_node(state)
    
    # Save updated state
    save_presentation(updated_state, presentation_id)
    
    return {"message": "Slide layout generated successfully.", "presentation_id": presentation_id, "slides_data": updated_state["slides_data"][presentation_index]}
   


#-------------------------------get presentation slides - generates slide code stream for each slide and returns as streaming response-------------------------------
@app.get("/presentation-slides/{presentation_id}",description="Generates slide code stream for each slide based on the presentation state and returns it as a streaming response.",tags=["Slide Code Generation"])
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