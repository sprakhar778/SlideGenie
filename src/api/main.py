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
from src.graph.nodes.slide_content_node import generate_slide_content_node
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

# In-memory storage
import json
PROJECTS_FILE = "projects_data.json"

def load_projects():
    try:
        with open(PROJECTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def make_json_serializable(obj):
    # Recursively convert Slide and other BaseModel objects to dicts
    if isinstance(obj, list):
        return [make_json_serializable(item) for item in obj]
    if hasattr(obj, "dict"):
        return obj.dict()
    if isinstance(obj, dict):
        return {k: make_json_serializable(v) for k, v in obj.items()}
    return obj

def save_projects():
    with open(PROJECTS_FILE, "w", encoding="utf-8") as f:
        json.dump(make_json_serializable(projects), f, ensure_ascii=False, indent=2)

projects: Dict[str, dict] = load_projects()


# -------------------------------
# Models
# -------------------------------

class ProjectCreateRequest(BaseModel):
    project_name: str


class TopicContentRequest(BaseModel):
    topic: str
    content: str


# -------------------------------
# Utility
# -------------------------------

def initial_state():
    return {
        "topic": "",
        "content": "",
        "theme_info": "",
        "slides_data": [],
       
   
        "slides": []
    }


def get_project(project_id: str):
    if project_id not in projects:
        raise HTTPException(status_code=404, detail="Project not found")
    return projects[project_id]


# -------------------------------
# Project APIs
# -------------------------------


# -------------------------------
# Project Management APIs
# -------------------------------

@app.post("/projects", tags=["Project Management"], summary="Create a new project")
def create_project(request: ProjectCreateRequest):
    project_id = str(uuid.uuid4())
    projects[project_id] = {
        "project_name": request.project_name,
        "session_id": str(uuid.uuid4()),
        "state": initial_state()
    }
    save_projects()
    logging.info(f"[API] Project created: {project_id} - {request.project_name}")
    return {
        "message": "Project created",
        "project_id": project_id,
        "session_id": projects[project_id]["session_id"],
        "state": projects[project_id]["state"]
    }



@app.post("/projects/{project_id}/input", tags=["Project Management"], summary="Set topic and content for a project")
def set_topic_content(project_id: str, request: TopicContentRequest):
    project = get_project(project_id)
    project["state"]["topic"] = request.topic
    project["state"]["content"] = request.content
    save_projects()
    logging.info(f"[API] Set topic/content for project {project_id}: topic='{request.topic}', content='{request.content[:40]}...")
    return {
        "message": "Topic and content set successfully",
        "topic": project["state"]["topic"],
        "content": project["state"]["content"]
    }



@app.get("/projects/{project_id}", tags=["Project Management"], summary="Get the full state of a project")
def get_project_state(project_id: str):
    project = get_project(project_id)
    return {"state": project["state"]}



# -------------------------------
# Node Processing APIs
# -------------------------------

@app.post("/projects/{project_id}/theme", tags=["Node Processing"], summary="Generate theme info for a project")
def run_theme_node(project_id: str):
    project = get_project(project_id)
    state = project["state"]
    state = generate_theme_node(state)
    project["state"] = state
    save_projects()
    logging.info(f"[API] Theme node run for project {project_id}")
    return {"theme_info": state["theme_info"], "state": state}


@app.post("/projects/{project_id}/slides-data", tags=["Node Processing"], summary="Generate slides data for a project")
def run_slides_data_node(project_id: str):
    project = get_project(project_id)
    state = project["state"]
    state = generate_slides_data_node(state)
    project["state"] = state
    save_projects()
    logging.info(f"[API] Slides-data node run for project {project_id}")
    return {"slides_data": state["slides_data"], "state": state}


@app.post("/projects/{project_id}/generate-all", tags=["Node Processing"], summary="Run layout, content, and generator for all slides in sequence, parallel per slide")
def run_full_pipeline(project_id: str):
    import asyncio
    import os
    from pathlib import Path
    
    project = get_project(project_id)
    state = project["state"]

    logging.info(f"[API] Full pipeline started for project {project_id}")

    # 1. Ensure slides_data exists
    if not state.get("slides_data") or len(state["slides_data"]) == 0:
        logging.warning(f"[API] Full pipeline: slides_data missing for project {project_id}")
        raise HTTPException(status_code=400, detail="slides_data must be generated first.")

    topic = state["topic"]
    content = state["content"]
    theme_info = state.get("theme_info", "")
    slides = state["slides_data"]

    # --- Step 1: Layouts in parallel ---
    from src.chains.slide_layout_chain import select_slide_layout
    async def layout_for_slide(slide):
        if isinstance(slide, dict):
            slide_type = slide.get("slide_type")
        else:
            slide_type = getattr(slide, "slide_type", None)
        if not slide_type:
            raise ValueError(f"Invalid slide_type: {slide_type} for slide: {slide}")
        return select_slide_layout(topic=topic, content=content, slide_type=slide_type)
    async def gather_layouts():
        return await asyncio.gather(*(layout_for_slide(slide) for slide in slides))
    layouts = asyncio.run(gather_layouts())
    state["slides_layout"] = layouts
    logging.info(f"[API] Layouts generated for project {project_id}")

    # --- Step 2: Content in parallel ---
    from src.chains.slide_content_chain import get_slide_content_chain
    async def content_for_slide(slide, layout):
        slide_type = getattr(slide, "slide_type", None)
        description = getattr(slide, "description", None)
        return await get_slide_content_chain(
            topic=topic,
            content=content,
            slide_type=slide_type,
            description=description
        )
    async def gather_contents():
        return await asyncio.gather(*(content_for_slide(slide, layout) for slide, layout in zip(slides, layouts)))
    slide_contents = asyncio.run(gather_contents())
    state["slide_content"] = slide_contents
    state["slides_content"] = slide_contents  # for frontend compatibility
    logging.info(f"[API] Slide content generated for project {project_id}")

    # --- Step 3: Generator in parallel ---
    from src.chains.slide_generator_chain import get_slide_generator_chain
    async def generator_for_slide(i):
        slide = slides[i]
        layout = layouts[i]
        content_val = slide_contents[i]
        slide_type = getattr(slide, "slide_type", None)
        layout_name = getattr(layout, "layout_name", None) if hasattr(layout, "layout_name") else layout.get("layout_name")
        components = getattr(layout, "components", None) if hasattr(layout, "components") else layout.get("components")
        return await get_slide_generator_chain(
            topic=topic,
            content=content_val,
            theme_info=theme_info,
            slide_type=slide_type,
            layout_name=layout_name,
            components=components
        )
    async def gather_generators():
        return await asyncio.gather(*(generator_for_slide(i) for i in range(len(slides))))
    slides_html = asyncio.run(gather_generators())
    state["slides"] = slides_html
    
    # --- Save HTML slides to separate files ---
    # Create a folder for this project's slides
    slides_folder = Path(f"generated_slides/{project_id}")
    slides_folder.mkdir(parents=True, exist_ok=True)
    
    # Save each slide as a separate HTML file
    saved_files = []
    for i, slide_html in enumerate(slides_html):
        # Sanitize slide type for filename
        slide_type = slides[i].get("slide_type", f"slide_{i+1}") if isinstance(slides[i], dict) else f"slide_{i+1}"
        # Remove any invalid filename characters
        slide_type = "".join(c for c in slide_type if c.isalnum() or c in (' ', '-', '_')).rstrip()
        
        filename = f"{i+1:02d}_{slide_type}.html"
        filepath = slides_folder / filename
        
        # Write the HTML content to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(slide_html)
        
        saved_files.append(str(filepath))
        logging.info(f"[API] Saved slide {i+1} to {filepath}")
    
    # Also create an index.html that links all slides
    index_path = slides_folder / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(f"""<!DOCTYPE html>
<html>
<head>
    <title>Slides for Project {project_id}</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        h1 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 10px 0; }}
        a {{ text-decoration: none; color: #0066cc; padding: 5px 10px; border: 1px solid #ddd; border-radius: 3px; }}
        a:hover {{ background-color: #f0f0f0; }}
    </style>
</head>
<body>
    <h1>Slides for Project: {project_id}</h1>
    <h2>Topic: {topic}</h2>
    <ul>
""")
        for i, filename in enumerate([f.name for f in slides_folder.glob("*.html") if f.name != "index.html"]):
            f.write(f'        <li><a href="{filename}" target="_blank">Slide {i+1}: {filename.replace(".html", "")}</a></li>\n')
        f.write("""    </ul>
</body>
</html>""")
    
    logging.info(f"[API] All slides saved to folder: {slides_folder.absolute()}")
    
    project["state"] = state
    save_projects()
    logging.info(f"[API] Full pipeline complete for project {project_id}")
    
    return {
        "message": "All slide steps completed in sequence (parallel per slide)",
        "slides_layout": layouts,
        "slides_content": slide_contents,
        "slides": slides_html,
        "saved_files": saved_files,
        "slides_folder": str(slides_folder.absolute()),
        "state": state
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=8000, reload=True)