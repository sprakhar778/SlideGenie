from fastapi import FastAPI
from src.graph.nodes.theme_node import generate_theme_node
from src.graph.nodes.slides_data_node import generate_slides_data_node
from src.graph.nodes.slide_layout_node import generate_slide_layout_node
from src.graph.nodes.slide_content_node import generate_slide_content_node
from src.graph.nodes.slide_generator_node import generate_slides_node


def initial_state():
    {
        "topic":"",
        "content":"",
        "theme_info":"",
        #slide_type,content,description
        "slides_data":[],
        #layout_name,rational,components
        "slides_layout":[],
        #slide_content
        "slides_content":[],
        
    }

    
