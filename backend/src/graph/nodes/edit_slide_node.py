from src.chains.edit_slide_code_chain import stream_edit_slide_code_chain

async def edit_slide_node(state: dict, slide_index: int, user_input: str):
    """
    Streams the edited slide code back to the client based on user input and the existing slide code.
    Reads the existing slide_code from the state.
    """
    slides_data = state.get("slides_data", [])
    theme_info = state.get("theme_info", [])

    if slide_index < 0 or slide_index >= len(slides_data):
        raise ValueError(f"Slide index {slide_index} out of range.")
        
    slide_code = slides_data[slide_index].get("slide_code", "")
    slide_layout = slides_data[slide_index].get("layout", "")   
    slide_content = slides_data[slide_index].get("content", "")
    
    if not slide_code:
        raise ValueError(f"No existing slide code found for slide index {slide_index}.")

    async for token in stream_edit_slide_code_chain(theme_info,slide_layout,slide_code, user_input,slide_content):
        yield {
            "slide_index": slide_index,
            "token": token,
        }
        
    yield {
        "slide_index": slide_index,
        "done": True,
    }
