from src.chains.slide_generator_chain import get_slide_generator_chain
from src.graph.state import PresentationState

def generate_slides_node(state: PresentationState) -> PresentationState:
    """Node to generate slides based on the presentation state."""
    
    if not state.get("content") or not state.get("topic"):
        raise ValueError("Both 'content' and 'topic' must be provided in the state.")
    
    # Generate slides using the chain
    generated_slides = get_slide_generator_chain(
        topic=state["topic"],
        content=state["content"]
    )
    
    # Update the state with the generated slides
    state["slides"] = generated_slides
    
    return state