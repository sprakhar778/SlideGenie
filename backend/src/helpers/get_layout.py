from src.prompts.slide_layout_prompts.hero import HERO_SLIDE_LAYOUT
from src.prompts.slide_layout_prompts.agenda import AGENDA_SLIDE_LAYOUT
from src.prompts.slide_layout_prompts.key_points import KEY_POINTS_SLIDE_LAYOUT
from src.prompts.slide_layout_prompts.concept_explain import CONCEPT_EXPLAIN_SLIDE_LAYOUT
from src.prompts.slide_layout_prompts.flow import FLOW_SLIDE_LAYOUT
from src.prompts.slide_layout_prompts.comparison import COMPARISON_SLIDE_LAYOUT
from src.prompts.slide_layout_prompts.visual_led import VISUAL_SLIDE_LAYOUT
from src.prompts.slide_layout_prompts.evidence import EVIDENCE_SLIDE_LAYOUT
from src.prompts.slide_layout_prompts.summary import SUMMARY_SLIDE_LAYOUT
from src.prompts.slide_layout_prompts.thanks import THANK_YOU_SLIDE_LAYOUT
import random
SLIDE_TYPE_TO_LAYOUT = {
    "Hero": HERO_SLIDE_LAYOUT,
    "Agenda": AGENDA_SLIDE_LAYOUT,
    "Key Points": KEY_POINTS_SLIDE_LAYOUT,
    "Concept Explanation": CONCEPT_EXPLAIN_SLIDE_LAYOUT,
    "Process": FLOW_SLIDE_LAYOUT,
    "Comparison": COMPARISON_SLIDE_LAYOUT,
    "Visual Emphasis": VISUAL_SLIDE_LAYOUT,
    "Data": EVIDENCE_SLIDE_LAYOUT,
    "Summary": SUMMARY_SLIDE_LAYOUT,
    "Thank You": THANK_YOU_SLIDE_LAYOUT,
}


def get_layout(slide_type,k=None):
    """
    Get the layout json for a given slide type.
    
   
    """
    layout = SLIDE_TYPE_TO_LAYOUT.get(slide_type)

    if not layout:
        raise ValueError(f"Invalid slide type: {slide_type}")
    
    if k and 1<=k<=len(list(layout.keys())):
        random_key=str(k)
    else:
        random_key = random.choice(list(layout.keys()))

    selected_layout=layout[random_key]

    layout_info = "\n".join([
        f"Name: {selected_layout['name']}",
        f"Purpose: {selected_layout['purpose']}",
        f"Structure: {selected_layout['structure']}"
    ])
    
    return layout_info


# x=get_layout("Hero")
# print(x)

    