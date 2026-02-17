from src.chains.slide_content_chain import get_slide_content_chain



def generate_slide_content_node(state):
    """Node to generate slide content based on the presentation state."""
    
    if not state.get("content") or not state.get("topic"):
        raise ValueError("Both 'content' and 'topic' must be provided in the state.")
    
    # For simplicity, we will generate content for a single slide type (e.g., "Process")
    topic = state["topic"]
    content = state["content"]

    slides = state.get("slides_data")

    for i in range(len(slides)):
        slide_type = slides[0]["slide_type"] 
        slide_description = slides[0]["description"] 
        
        # Generate slide content using the chain
        generated_content = get_slide_content_chain(
            topic=topic,
            content=content,
            slide_type=slide_type,
            slide_description=slide_description
            
        )
        
        # Update the state with the generated slide content
        state["slide_content"].append(generated_content)
    
    return state