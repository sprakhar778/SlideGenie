
from src.helpers.get_layout import get_layout

def generate_slide_layout_node(state):
    """Node to select slide layout based on topic, content, and slide type."""
    
    if not state.get("content") or not state.get("topic"):
        raise ValueError("Both 'content' and 'topic' must be provided in the state.")

    topic = state["topic"]
    content = state["content"]
    
    slides = state.get("slides_data")

    for i in range(len(slides)):
        slide=slides[i]
        slide_type = slide["slide_type"] 

        # 🔹 Call layout selection chain
        slide_layout = get_layout(slide_type)

        # 🔹 Store structured layout inside state
        slide["layout"]=slide_layout
    
   

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

