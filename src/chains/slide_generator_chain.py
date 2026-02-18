from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from src.prompts.slide_design_prompt import SLIDE_DESIGN_PROMPT 
from src.llm.llm_provider import get_llm
from src.helpers.clean_text import clean_html_output
from dotenv import load_dotenv
import asyncio
load_dotenv()


async def get_slide_generator_chain(topic:str,theme_info:str,slide_data):
    """Generate slide HTML based on the given topic and content."""
    # Initialize Gemini chat model
    slide_type=slide_data["slide_type"]
    slide_content=slide_data["content"]
    slide_description=slide_data["description"]
    slide_layout=slide_data["layout"]

    llm=get_llm()


    # -------- Chain 2: topic + manifesto + content → HTML --------
    slide_prompt = PromptTemplate(
        template=SLIDE_DESIGN_PROMPT,
        input_variables=[
            "topic", 
            "slide_content",
            "theme_info",
            "slide_type",
            "slide_layout",

           


           
        ]
    )

    chain = slide_prompt | llm | StrOutputParser() | RunnableLambda(clean_html_output)

    result=chain.invoke(
        {
            "topic":topic,
            "content":slide_content,
            "theme_info":theme_info,
            "slide_type":slide_type,
            "slide_layout":slide_layout
           
        }
    )
    return result



 


    # 2. Now the invoke only needs the variables that AREN'T partialed
  



# -------- Run --------
# result = agent.invoke({
#     "topic": "Future of AI in Healthcare",
#     "content": """
#     - AI-powered diagnostics
#     - Predictive patient risk models
#     - Personalized medicine
#     - Hospital workflow automation
#     """
# })
# Updated topic: Sustainable Energy Transition
import asyncio

if __name__ == "__main__":

    async def main():
        result = await get_slide_generator_chain(
            topic="Future of AI in Healthcare",
            content="""
            - AI-powered diagnostics
            - Predictive patient risk models
            - Personalized medicine
            - Hospital workflow automation
            """,
            theme_info="Modern clean minimal theme with green and blue gradient accents",
            slide_type="content",
            layout_name=" ",
            components="title, bullet_points, icon_section"
        )

        # Save HTML
        with open("slides.html", "w", encoding="utf-8") as f:
            f.write(result)

        print("✅ slides.html generated successfully")

    asyncio.run(main())
