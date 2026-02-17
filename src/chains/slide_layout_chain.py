
from langchain_core.prompts import PromptTemplate
from src.llm.llm_provider import get_llm
from src.helpers.get_layout_prompt import get_layout_prompt
from src.models.slide_layout_models  import SlideLayout
from dotenv import load_dotenv
load_dotenv()


def select_slide_layout(topic: str, content: str,slide_type: str):
    content_summary = content[:300]  # Use only the first 300 characters for layout selection
    prompt_template = get_layout_prompt(slide_type) 
    prompt=PromptTemplate(
        template=prompt_template,
        input_variables=["topic", "content"]
        
     )
    llm=get_llm().with_structured_output(SlideLayout)

    chain= prompt | llm

    slide_layout = chain.invoke({
        "topic": topic,
        "content": content_summary
    })
    print(f"Selected layout for {slide_type}")
    print(f"Layout Name: {slide_layout.layout_name}")
    print(f"Rationale: {slide_layout.rationale}")
    print(f"Components: {', '.join(slide_layout.components)}")
          
    return slide_layout


# if __name__ == "__main__":
#     topic = "The Future of Artificial Intelligence"
#     content = (
  
#         "Finally, we will look ahead to long-term possibilities such as artificial general intelligence (AGI), superintelligence, and AI alignment challenges. "
#         "The presentation concludes by reflecting on how AI can be harnessed responsibly for positive societal impact, sustainability, scientific discovery, and global problem-solving."
#     )
#     select_slide_layout(topic=topic , content=content , slide_type="Summary")



