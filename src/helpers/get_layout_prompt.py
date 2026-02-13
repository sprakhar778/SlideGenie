from src.prompts.slide_layout_prompts.hero import HERO_SLIDE_LAYOUT_PROMPT
from src.prompts.slide_layout_prompts.agenda import AGENDA_SLIDE_LAYOUT_PROMPT
from src.prompts.slide_layout_prompts.key_points import KEY_POINTS_SLIDE__LAYOUT_PROMPT
from src.prompts.slide_layout_prompts.concept_explain import CONCEPT_EXPLAIN_SLIDE_LAYOUT_PROMPT
from src.prompts.slide_layout_prompts.flow import FLOW_SLIDE_LAYOUT_PROMPT
from src.prompts.slide_layout_prompts.comparison import COMPARISON_SLIDE_LAYOUT_PROMPT
from src.prompts.slide_layout_prompts.visual_led import VISUAL_SLIDE_LAYOUT_PROMPT
from src.prompts.slide_layout_prompts.evidence import EVIDENCE_SLIDE_LAYOUT_PROMPT
from src.prompts.slide_layout_prompts.summary import SUMMARY_SLIDE_LAYOUT_PROMPT
from src.prompts.slide_layout_prompts.thanks import THANK_YOU_SLIDE_LAYOUT_PROMPT
SLIDE_TYPE_TO_PROMPT = {
    "Hero": HERO_SLIDE_LAYOUT_PROMPT,
    "Agenda": AGENDA_SLIDE_LAYOUT_PROMPT,
    "Key Points": KEY_POINTS_SLIDE__LAYOUT_PROMPT,
    "Concept Explanation": CONCEPT_EXPLAIN_SLIDE_LAYOUT_PROMPT,
    "Process": FLOW_SLIDE_LAYOUT_PROMPT,
    "Comparison": COMPARISON_SLIDE_LAYOUT_PROMPT,
    "Visual Emphasis": VISUAL_SLIDE_LAYOUT_PROMPT,
    "Data": EVIDENCE_SLIDE_LAYOUT_PROMPT,
    "Summary": SUMMARY_SLIDE_LAYOUT_PROMPT,
    "Thank You": THANK_YOU_SLIDE_LAYOUT_PROMPT,
}


def get_layout_prompt(slide_type):
    """
    Get the layout prompt for a given slide type.
    
    Args:
        slide_type: The type of slide (must be one of the supported types)
        
    Returns:
        The prompt string for the given slide type
        
    Raises:
        ValueError: If the slide type is invalid
    """
    prompt = SLIDE_TYPE_TO_PROMPT.get(slide_type)
    if not prompt:
        raise ValueError(f"Invalid slide type: {slide_type}")
    
    return prompt
