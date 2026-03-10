from src.prompts.image_planner_prompt import IMAGE_PLANNER_PROMPT
from src.llm.llm_provider import get_llm
from langchain_core.prompts import PromptTemplate
from src.models.image_planner_model import ImagePlanList
from src.helpers.unsplash_image import fetch_unsplash_image_url
import asyncio


async def get_image_planner_chain(topic: str, content: str, layout: str) -> list[dict]:
    llm = get_llm(streaming=False).with_structured_output(ImagePlanList)

    image_planner_prompt = PromptTemplate(
        template=IMAGE_PLANNER_PROMPT,
        input_variables=["topic", "content", "layout"]
    )

    image_planner_chain = image_planner_prompt | llm

    result: ImagePlanList = await image_planner_chain.ainvoke(
        {"topic": topic, "content": content, "layout": layout}
    )

    plans = result.image_plan_list  # list[ImagePlan]

    # If LLM decided no images are needed, return empty list immediately (no API calls)
    if not plans:
        return []

    # Fetch all Unsplash URLs concurrently
    async def fetch(plan) -> dict:
        url = await fetch_unsplash_image_url(plan.search_query)
        return {
            "image_keywords": plan.image_keywords,
            "search_query": plan.search_query,
            "image_description": plan.image_description,
            "image_url": url or "none",
        }

    image_plan_dict = await asyncio.gather(*[fetch(p) for p in plans])
    return list(image_plan_dict)


def format_image_plan(image_plan: list[dict]) -> str:
    """Formats image plan list into a readable block to inject into the slide design prompt."""
    if not image_plan:
        return "No images are needed for this slide. Do NOT add any <img> tags."

    lines = ["Pre-fetched images for this slide (use in order):"]
    for i, img in enumerate(image_plan, 1):
        lines.append(f"  IMAGE {i}:")
        lines.append(f"    URL:         {img['image_url']}")
        lines.append(f"    Keywords:    {img['image_keywords']}")
        lines.append(f"    Placement:   {img['image_description']}")
    return "\n".join(lines)