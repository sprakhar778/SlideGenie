from src.chains.slides_data_chain import get_slides_data_chain
from src.graph.state import PresentationState


def generate_slides_data_node(state: PresentationState) -> PresentationState:
    """Node to generate slides data based on the presentation state."""
    
    if not state.get("content") or not state.get("topic"):
        raise ValueError("Both 'content' and 'topic' must be provided in the state.")
    
    # Generate slides data using the chain
    generated_slides_data = get_slides_data_chain(
        topic=state["topic"],
        content=state["content"]
    )
    
    # Update the state with the generated slides data
    state["slides_data"] = generated_slides_data
    
    return state