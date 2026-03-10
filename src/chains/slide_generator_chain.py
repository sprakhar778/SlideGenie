from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from src.prompts.slide_design_prompt import SLIDE_DESIGN_PROMPT 
from src.llm.llm_provider import get_llm
from src.helpers.clean_text import clean_html_output
from src.chains.image_planner_chain import get_image_planner_chain, format_image_plan
from dotenv import load_dotenv
import asyncio
load_dotenv()


    
async def stream_slide_generator_chain(topic: str, theme_info: str, slide_data):
    slide_type = slide_data["slide_type"]
    slide_content = slide_data["content"]
    slide_layout = slide_data["layout"]
    
    #for geeting image plan dict {}
    image_plan_list = await get_image_planner_chain(topic, slide_content, slide_layout)
    image_plan = format_image_plan(image_plan_list)
    

    

    llm = get_llm(streaming=True)

    slide_prompt = PromptTemplate(
        template=SLIDE_DESIGN_PROMPT,
        input_variables=[
            "topic",
            "slide_content",
            "theme_info",
            "slide_type",
            "slide_layout",
            "image_plan",
           
        ],
    )

    chain = slide_prompt | llm | StrOutputParser()

    async for chunk in chain.astream(
        {
            "topic": topic,
            "slide_content": slide_content,
            "theme_info": theme_info,
            "slide_type": slide_type,
            "slide_layout": slide_layout,
            "image_plan": image_plan,
        }
    ):
        yield chunk



# if __name__ == "__main__":
#     # 1. You can test the slide generator chain in isolation with hardcoded values
#     topic = "Sustainable Energy Solutions"

#     theme_info = "A modern, clean design with green and blue accents to reflect the sustainability theme."
#     slide_data = {
#         "slide_type": "Title Slide",
#         "content": "Introduction to Sustainable Energy Solutions",
#         "layout": "Title and Subtitle"
#     }

#     async def test_slide_generator():
#         async for chunk in stream_slide_generator_chain(topic, theme_info, slide_data):
#             print(chunk, end="", flush=True)

#     asyncio.run(test_slide_generator())

#python -m src.chains.slide_generator_chain