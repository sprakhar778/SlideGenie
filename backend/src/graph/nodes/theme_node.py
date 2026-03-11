from src.chains.theme_chain import get_theme_chain



def generate_theme_node(state):
    """Node to generate theme information based on the presentation state."""
    topic=state.get("topic")
    content=state.get("content")
    if not state.get("topic"):
        raise ValueError("The 'topic' must be provided in the state.")
    
    # Generate theme information using the chain
    generated_theme_info = get_theme_chain(topic=topic, content=content)
    
    # Update the state with the generated theme information
    state["theme_info"] = generated_theme_info
    
    return state