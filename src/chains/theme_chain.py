from typing import Optional

from langchain_core.prompts import PromptTemplate

from src.llm.llm_provider import get_llm
from src.prompts.theme_prompt import THEME_PROMPT
from src.models.theme_models import Theme
from src.helpers.theme_info import get_theme_info


def get_theme_chain(topic: str, content: Optional[str]):
    """Generate a presentation theme based on the given topic and content."""

    # Initialize LLM with structured output
    llm = get_llm().with_structured_output(Theme)

    # Build prompt
    theme_prompt = PromptTemplate(
        input_variables=["topic", "content"],
        template=THEME_PROMPT,
    )

    # Truncate content to stay within token limits
    content = content[:1000] if content else ""

    # Create chain
    theme_chain = theme_prompt | llm

    # Invoke chain
    theme = theme_chain.invoke(
        {"topic": topic, "content": content}
    )

    # Fetch theme metadata
    theme_info = get_theme_info(theme.theme)

    print(f"Selected Theme: {theme.theme}")
    print(f"Description: {theme_info}")

    return theme_info


if __name__ == "__main__":
    topic = "Sustainable Energy Solutions"
    content = (
        "This presentation will cover various sustainable energy solutions, "
        "including solar, wind, and hydroelectric power. We will discuss the "
        "benefits of each solution, their environmental impact, and how they "
        "can be implemented in different regions around the world. The goal "
        "is to provide a comprehensive overview of sustainable energy options "
        "and encourage adoption for a greener future."
    )

    selected_theme = get_theme_chain(topic, content)
