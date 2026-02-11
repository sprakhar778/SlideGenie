# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableLambda
# from langchain_google_genai import ChatGoogleGenerativeAI
# from pydantic import BaseModel, Field
# from enum import Enum
# from prompts.slide_prompt import SLIDE_PROMPT
# from typing import List, Optional,Literal
# import re
# load_dotenv()



# class SlideType(str, Enum):
#     HERO = "Hero"
#     AGENDA = "Agenda"
#     KEY_POINTS = "Key Points"
#     CONCEPT_EXPLANATION = "Concept Explanation"
#     PROCESS = "Process"
#     COMPARISON = "Comparison"
#     VISUAL_EMPHASIS = "Visual Emphasis"
#     DATA = "Data"
#     SUMMARY = "Summary"
#     THANK_YOU = "Thank You"



# class Slide(BaseModel):
#     slide_type: SlideType = Field(
#         ...,
#         description="Type of the slide, selected from predefined slide categories"
#     )
#     content: str = Field(
#         ...,
#         description="Main textual content of the slide"
#     )
#     description: str | None = Field(
#         None,
#         description="Optional explanation or intent of the slide"
#     )



# class Slides(BaseModel):
#     slides: list[Slide] = Field(
#         ...,
#         description="Collection of slides forming the full presentation"
#     )



# # Initialize Gemini chat model
# llm = ChatGoogleGenerativeAI(model="gemini-3-pro-preview", temperature=0.3)

# llm=llm.with_structured_output(Slides)



# slide_prompt = PromptTemplate(
#     template=SLIDE_PROMPT,
#     input_variables=["topic",  "content"]
# )

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from enum import Enum
from prompts.slide_data_prompt import SLIDE_DATA_PROMPT
from typing import List, Optional, Literal
import re
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import json

load_dotenv()

# Initialize rich console for pretty printing
console = Console()

class SlideType(str, Enum):
    HERO = "Hero"
    AGENDA = "Agenda"
    KEY_POINTS = "Key Points"
    CONCEPT_EXPLANATION = "Concept Explanation"
    PROCESS = "Process"
    COMPARISON = "Comparison"
    VISUAL_EMPHASIS = "Visual Emphasis"
    DATA = "Data"
    SUMMARY = "Summary"
    THANK_YOU = "Thank You"


class Slide(BaseModel):
    slide_type: SlideType = Field(
        ...,
        description="Type of the slide, selected from predefined slide categories"
    )
    content: str = Field(
        ...,
        description="Main textual content of the slide"
    )
    description: str | None = Field(
        None,
        description="Optional explanation or intent of the slide"
    )


class Slides(BaseModel):
    slides: list[Slide] = Field(
        ...,
        description="Collection of slides forming the full presentation"
    )


def display_slides_nicely(slides: Slides):
    """Display slides in an organized, readable format using rich."""
    
    # Display overall presentation info
    console.print(Panel.fit(
        f"[bold cyan]Presentation Generated Successfully![/bold cyan]\n"
        f"[bold]Total Slides:[/bold] {len(slides.slides)}\n",
        title="📊 Presentation Summary",
        border_style="cyan"
    ))
    
    # Display slides in a table
    table = Table(title="🎯 Presentation Slides", show_header=True, header_style="bold magenta")
    table.add_column("#", style="dim", width=4)
    table.add_column("Slide Type", style="cyan", width=20)
    table.add_column("Content Preview", style="white", width=60)
    table.add_column("Description", style="green", width=30)
    
    for idx, slide in enumerate(slides.slides, 1):
        # Truncate content for display
        content_preview = slide.content[:80] + "..." if len(slide.content) > 80 else slide.content
        description = slide.description or "No description provided"
        description_preview = description[:50] + "..." if len(description) > 50 else description
        
        table.add_row(
            str(idx),
            slide.slide_type.value,
            content_preview,
            description_preview
        )
    
    console.print(table)
    
    # Display detailed view of each slide
    console.print("\n[bold yellow]📋 Detailed Slide View:[/bold yellow]")
    for idx, slide in enumerate(slides.slides, 1):
        console.print(Panel(
            f"[bold]Content:[/bold] {slide.content}\n"
            f"[bold]Description:[/bold] {slide.description or 'N/A'}",
            title=f"Slide {idx}: {slide.slide_type.value}",
            border_style="blue" if idx % 2 == 0 else "green"
        ))
    
    # Display slide type distribution
    slide_counts = {}
    for slide in slides.slides:
        slide_type = slide.slide_type.value
        slide_counts[slide_type] = slide_counts.get(slide_type, 0) + 1
    
    console.print("\n[bold magenta]📈 Slide Type Distribution:[/bold magenta]")
    for slide_type, count in slide_counts.items():
        console.print(f"  • {slide_type}: {count} slide{'s' if count > 1 else ''}")


# Initialize Gemini chat model
llm = ChatGoogleGenerativeAI(model="gemini-3-pro-preview", temperature=0.3)
llm = llm.with_structured_output(Slides)

slide_prompt = PromptTemplate(
    template=SLIDE_DATA_PROMPT,
    input_variables=["topic", "content"]
)


def create_presentation_chain():
    """Create the chain for generating presentations."""
    return slide_prompt | llm


def invoke_agent(topic: str, content: str) -> Slides:
    """Invoke the agent to generate slides."""
    console.print(Panel.fit(
        f"[bold]Topic:[/bold] {topic}\n"
        f"[bold]Content Length:[/bold] {len(content)} characters",
        title="🚀 Generating Presentation",
        border_style="yellow"
    ))
    
    # Create the chain
    chain = create_presentation_chain()
    
    # Invoke the model
    console.print("[dim]Generating slides...[/dim]")
    result = chain.invoke({"topic": topic, "content": content})
    
    return result


# Example usage function
def main():
    """Example main function to demonstrate usage."""
    # Example data
    topic = "The Future of AI in Healthcare"
    content = """
    Artificial Intelligence is revolutionizing healthcare in multiple ways:
    1. Diagnostics: AI can analyze medical images with high accuracy
    2. Drug Discovery: Accelerating the development of new medications
    3. Personalized Medicine: Tailoring treatments to individual patients
    4. Administrative Automation: Streamlining hospital operations
    
    Key benefits include improved accuracy, reduced costs, and better patient outcomes.
    However, challenges remain in data privacy, regulatory compliance, and ethical considerations.
    
    The future looks promising with advancements in explainable AI and integration with IoT devices.
    """
    
    # Generate slides
    slides = invoke_agent(topic, content)
    
    # Display results nicely
    display_slides_nicely(slides)
    
    return slides


if __name__ == "__main__":
    # Run the example
    main()