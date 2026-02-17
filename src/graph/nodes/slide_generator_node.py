import os
from src.chains.slide_generator_chain import get_slide_generator_chain


def generate_slides_node(state):
    """Node to generate slides based on the presentation state."""

    if not state.get("content") or not state.get("topic"):
        raise ValueError("Both 'content' and 'topic' must be provided in the state.")

    slides = state.get("slides_data")
    state["slides"] = []

    # Folder where all slide files will be saved
    output_dir = "saved_slides"
    os.makedirs(output_dir, exist_ok=True)

    for i in range(len(slides)):

        topic = state["topic"]
        theme_info = state["theme_info"]
        content = state["slides_content"][i]
        slide_type = state["slides_data"][i]["slide_type"]
        slide_layout_name = state["slides_layout"][i]["layout_name"]
        components = state["slides_layout"][i]["components"]

        # Generate slide HTML
        generated_slide = get_slide_generator_chain(
            topic=topic,
            content=content,
            theme_info=theme_info,
            slide_type=slide_type,
            layout_name=slide_layout_name,
            components=components
        )

        state["slides"].append(generated_slide)

        # Save each slide as index1.html, index2.html, etc.
        file_path = os.path.join(output_dir, f"index{i+1}.html")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(generated_slide)

    print(f"✅ All slides saved inside '{output_dir}' folder")

    return state
