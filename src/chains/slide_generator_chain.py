from langchain_core.prompts import PromptTemplate

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from src.prompts.slide_design_prompt import SLIDE_DESIGN_PROMPT 
from src.llm.llm_provider import get_llm
from src.helpers.clean_text import clean_html_output
from dotenv import load_dotenv
load_dotenv()


def get_slide_generator_chain():
    """Generate slide HTML based on the given topic and content."""
    # Initialize Gemini chat model

    llm=get_llm()


    # -------- Chain 2: topic + manifesto + content → HTML --------
    slide_prompt = PromptTemplate(
        template=SLIDE_DESIGN_PROMPT,
        input_variables=[
            "topic", 
            "content", 

            "slide_type", 
            "heading_font", 
            "palette", 
            "body_font"
        ]
    )

    agent = slide_prompt | llm | StrOutputParser() | RunnableLambda(clean_html_output)



    # 1. Fix the template by pre-filling the design variables
    slide_prompt_fixed = slide_prompt.partial(
        
        slide_type="Process Flow",
        heading_font="Arial Bold",
        body_font="Calibri",
        palette="Corporate Blue/Grey"
    )


    # 2. Now the invoke only needs the variables that AREN'T partialed
    result = agent.invoke({
        "topic": "Future of AI in Healthcare ",
        "content": """
        - AI-powered diagnostics
        - Predictive patient risk models
        - Personalized medicine
        - Hospital workflow automation""",
        # These must match the names in your PromptTemplate exactly
        "components": "Bullets points with icons on the left, high-quality visual on the right",
        "slide_type": "Timeline/Process",
        "heading_font": "Arial Bold",
        "body_font": "Calibri",
        "palette": " **Hex:** `#F5F7FA, **Hex:** `#1F2933, **Hex:** `#2563EB"

            })

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
    result = get_slide_generator_chain()


    # -------- Save HTML --------
    with open("slides.html", "w", encoding="utf-8") as f:
        f.write(result)

    print("✅ slides.html generated successfully")
