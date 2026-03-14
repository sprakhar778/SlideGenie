
from src.helpers.get_layout import get_layout


def generate_slide_layout_node(state):
    """
    Assign layout templates to each slide based on slide_type.
    """

    if not state.get("content") or not state.get("topic"):
        raise ValueError(
            "Both 'content' and 'topic' must be provided in the state."
        )

    slides = state.get("slides_data")

    if not slides:
        raise ValueError("No slides found in state. slides_data is empty.")

    for slide in slides:

        slide_type = slide.get("slide_type")

        if not slide_type:
            raise ValueError("Slide missing 'slide_type'.")

        # Generate layout
        slide_layout = get_layout(slide_type)

        # Save layout to slide
        slide["layout"] = slide_layout

    # Update state
    state["slides_data"] = slides

    return state
        
# if __name__ == "__main__":

#     # Dummy state
#     test_state = {
#         "topic": "Artificial Intelligence",
#         "content": "This presentation explores AI trends and future impact.",
#         "slides_data": [
#             {
#                 "slide_type": "Hero",
#                 "content": "The Future of AI",
#                 "description": "Introduction slide"
#             },
#             {
#                 "slide_type": "Comparison",
#                 "content": "AI vs Human Intelligence",
#                 "description": "Comparison slide"
#             },
#             {
#                 "slide_type": "Summary",
#                 "content": "Key Takeaways",
#                 "description": "Closing summary"
#             }
#         ],
#         "slides": []
#     }

#     # Run node
#     updated_state = generate_slide_layout_node(test_state)

#     print("\n---- FINAL OUTPUT ----")
#     for slide in updated_state["slides_data"]:
#         print(slide)

# python -m src.graph.nodes.slide_layout_node
