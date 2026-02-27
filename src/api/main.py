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

def save_presentation(state, presentation_id):
    output_dir = "generated_presentations"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{presentation_id}.json")
    
    with open(output_path, "w") as f:
        json.dump(state, f, indent=4)
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
    
    with open(output_path, "r") as f:
        state = json.load(f)
    
    # Step 2: Generate theme
    updated_state = generate_theme_node(state)
    
    # Save updated state
    save_presentation(updated_state, presentation_id)
    
    return {"message": "Theme generated successfully.", "presentation_id": presentation_id}

@app.post("/presentation-theme/{presentation_id}")
def update_presentation_theme(presentation_id: str, request:str):
    # Load the presentation state
    output_path = os.path.join("generated_presentations", f"{presentation_id}.json")
    
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")
    
    with open(output_path, "r") as f:
        state = json.load(f)
    
    # Update theme info in state
    state["theme_info"] = request
    
    # Save updated state
    save_presentation(state, presentation_id)
    
    return {"message": "Theme updated successfully.", "presentation_id": presentation_id}

@app.get("/presentation-layout/{presentation_id}")
def get_presentation_layout(presentation_id: str):
    # Load the presentation state
    output_path = os.path.join("generated_presentations", f"{presentation_id}.json")
    
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")
    
    with open(output_path, "r") as f:
        state = json.load(f)
    
    # Step 3: Generate slide layout
    updated_state = generate_slide_layout_node(state)
    
    # Save updated state
    save_presentation(updated_state, presentation_id)
    
    return {"message": "Slide layout generated successfully.", "presentation_id": presentation_id}
   
@app.get("/presentation-data/{presentation_id}")
def get_presentation_data(presentation_id: str):
    # Load the presentation state
    output_path = os.path.join("generated_presentations", f"{presentation_id}.json")
    
    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")
    
    with open(output_path, "r") as f:
        state = json.load(f)
    
    # Step 4: Generate slides data
    updated_state = generate_slides_data_node(state)
    
    # Save updated state
    save_presentation(updated_state, presentation_id)
    
    return {"message": "Slides data generated successfully.", "presentation_id": presentation_id}

from fastapi.responses import StreamingResponse
import json

@app.get("/presentation-slides/{presentation_id}")
async def get_presentation_slides(presentation_id: str):

    output_path = os.path.join("generated_presentations", f"{presentation_id}.json")

    if not os.path.exists(output_path):
        raise HTTPException(status_code=404, detail="Presentation not found.")

    with open(output_path, "r") as f:
        state = json.load(f)

    # --- TEST MODE: Only stream first slide ---
    slides = state.get("slides_data", [])
    if slides:
        slides = [slides[0]]

    test_state = {**state, "slides_data": slides}

    slide_stream = await generate_slides_node(test_state)

    async def stream_generator():

        # 🔹 Start SSE immediately (prevents browser hanging)
        yield "data: {}\n\n"

        accumulated_code = {i: "" for i in range(len(slides))}

        async for item in slide_stream:

            if "token" in item:
                slide_idx = item["slide_index"]
                accumulated_code[slide_idx] += item["token"]

            yield f"data: {json.dumps(item)}\n\n"

        # --- Save final generated code ---
        for idx, code in accumulated_code.items():
            if idx < len(state["slides_data"]):
                state["slides_data"][idx]["slide_code"] = code

        save_presentation(state, presentation_id)

        yield f"data: {json.dumps({'status': 'completed'})}\n\n"

    return StreamingResponse(stream_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)


# python -m src.api.main