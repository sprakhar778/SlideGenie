from src.chains.slide_content_chain import get_slide_content_chain



def generate_slide_content_node(state):
    """Node to generate slide content for all slides in parallel based on the presentation state."""
    import asyncio

    if not state.get("content") or not state.get("topic"):
        raise ValueError("Both 'content' and 'topic' must be provided in the state.")

    topic = state["topic"]
    content = state["content"]
    slides = state.get("slides_data")


    async def generate_for_slide(slide):
        slide_type = getattr(slide, "slide_type", None)
        slide_description = getattr(slide, "description", None)
        return await get_slide_content_chain(
            topic=topic,
            content=content,
            slide_type=slide_type,
            description=slide_description
        )

    async def gather_all():
        return await asyncio.gather(*(generate_for_slide(slide) for slide in slides))

    # Run all slide content generations in parallel
    state["slide_content"] = asyncio.run(gather_all())
    return state