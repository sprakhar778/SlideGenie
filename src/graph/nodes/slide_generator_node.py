import os
from src.chains.slide_generator_chain import get_slide_generator_chain


def generate_slides_node(state):
    """Node to generate slides in parallel based on the presentation state."""
    import asyncio

    if not state.get("content") or not state.get("topic"):
        raise ValueError("Both 'content' and 'topic' must be provided in the state.")

    slides = state.get("slides_data")
    state["slides"] = []

    output_dir = "saved_slides"
    os.makedirs(output_dir, exist_ok=True)

    topic = state["topic"]
    theme_info = state["theme_info"]

    async def generate_for_slide(i):
        content = state["slides_content"][i]
        slide_type = state["slides_data"][i]["slide_type"]
        slide_layout_name = state["slides_layout"][i]["layout_name"]
        components = state["slides_layout"][i]["components"]
        generated_slide = await get_slide_generator_chain(
            topic=topic,
            content=content,
            theme_info=theme_info,
            slide_type=slide_type,
            layout_name=slide_layout_name,
            components=components
        )
        file_path = os.path.join(output_dir, f"index{i+1}.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(generated_slide)
        return generated_slide

    async def gather_all():
        return await asyncio.gather(*(generate_for_slide(i) for i in range(len(slides))))

    # Run all slide generations in parallel
    state["slides"] = asyncio.run(gather_all())
    print(f"\u2705 All slides saved inside '{output_dir}' folder")
    return state
