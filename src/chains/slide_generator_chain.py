from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from src.prompts.slide_design_prompt import SLIDE_DESIGN_PROMPT 
from src.llm.llm_provider import get_llm
from src.helpers.clean_text import clean_html_output
from dotenv import load_dotenv
load_dotenv()


def get_slide_generator_chain(topic:str,content:str,theme_info:str,slide_type:str,components:str,layout_name:str):
    """Generate slide HTML based on the given topic and content."""
    # Initialize Gemini chat model

    llm=get_llm()


    # -------- Chain 2: topic + manifesto + content → HTML --------
    slide_prompt = PromptTemplate(
        template=SLIDE_DESIGN_PROMPT,
        input_variables=[
            "topic", 
            "content", 
             "theme_info",
            "slide_type", 
            "layout_name",
            "componets",

           
        ]
    )

    chain = slide_prompt | llm | StrOutputParser() | RunnableLambda(clean_html_output)

    result=chain.invoke(
        {
            "topic":topic,
            "content":content,
            "theme_info":theme_info,
            "slide_type":slide_type,
            "layout_name":layout_name,
            "components":components,
        }
    )



 


    # 2. Now the invoke only needs the variables that AREN'T partialed
  

    return result

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
if __name__ == "__main__":
    result = get_slide_generator_chain(
        topic="Sustainable Energy Transition",
        content="""
        - Shift from fossil fuels to renewables
        - Solar and wind power growth
        - Grid modernization
        - Energy storage technologies
        - Policy and climate goals
        """,
        theme_info="Modern clean minimal theme with green and blue gradient accents",
        slide_type="content",
        layout_name=" ",
        components="title, bullet_points, icon_section"
    )

    # -------- Save HTML --------
    with open("slides.html", "w", encoding="utf-8") as f:
        f.write(result)

    print("✅ slides.html generated successfully")
