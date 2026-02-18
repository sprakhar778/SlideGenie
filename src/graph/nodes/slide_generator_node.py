import os
from src.chains.slide_generator_chain import get_slide_generator_chain


def generate_slides_node(state):
    """Node to generate slides in parallel based on the presentation state."""
    topic=state["topic"]
    theme=state["theme_info"]
    slides_code=state["slides_code"]
    #list of dicts
    slides_data=state["slides_data"]
    for slide_data in slides_data:
        slides_code_result=get_slide_generator_chain(topic=topic,theme_info=theme,slide_data=slide_data)
        slides_code.append(slides_code_result)
    
    return state


