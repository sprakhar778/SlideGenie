from src.chains.slide_layout_chain import select_slide_layout

def generate_slide_layout_node(state):
    """Node to select slide layout based on topic, content, and slide type."""
    
    if not state.get("content") or not state.get("topic"):
        raise ValueError("Both 'content' and 'topic' must be provided in the state.")

    topic = state["topic"]
    content = state["content"]
    
    slides = state.get("slides_data")

    for i in range(len(slides)):
        slide_type = slides[i]["slide_type"] 

        # 🔹 Call layout selection chain
        slide_layout = select_slide_layout(
            topic=topic,
            content=content,
            slide_type=slide_type
        )

        # 🔹 Store structured layout inside state
        state["slide_layout"].appende(slide_layout)

    return state
