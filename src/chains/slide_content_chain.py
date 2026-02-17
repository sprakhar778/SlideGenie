from src.prompts.slide_content_prompt import SLIDE_CONTENT_PROMPT
from src.llm.llm_provider import get_llm
from langchain_core.prompts import PromptTemplate
from src.models.slide_content_models import SlideContent



def get_slide_content_chain(topic: str, content: str, slide_type: str,description: str):
    """Generate slide content based on the given topic, content, and slide type."""
   
    # Initialize LLM with structured output
    llm = get_llm().with_structured_output(SlideContent)

    # Build prompt
    slide_content_prompt = PromptTemplate(
        template=SLIDE_CONTENT_PROMPT,
        input_variables=["topic", "content", "slide_type", "description"]
    )

    # Create chain
    slide_content_chain = slide_content_prompt | llm

    # Invoke chain
    slide_content = slide_content_chain.invoke(
        {"topic": topic, "content": content, "slide_type": slide_type, "description": description}
    )
    
    print(f"Generated Content for {slide_type} Slide:\n{slide_content.slide_content}")
    
    return slide_content.slide_content


# if __name__ == "__main__":
#     # Example usage matching your provided case
#     topic = "The Future of Artificial Intelligence"
#     raw_content = (
#         "We begin by examining the evolution of artificial intelligence, tracing its "
#         "development from early rule-based systems to modern deep learning models. "
#         "This historical context provides a framework for understanding the current state."
#     )
    
#     # Example 1: Process Slide
#     res=get_slide_content_chain(
#         topic=topic, 
#         content=raw_content, 
#         slide_type="Process",
#         description="Chronological progression from rule-based systems to deep learning."
#     )

   