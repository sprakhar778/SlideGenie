from pydantic import BaseModel, Field
from typing import List, Optional, Literal




class Slide(BaseModel):
    slide_type: Literal["Hero", "Agenda", "Key Points", "Concept Explanation", "Process", "Comparison", "Visual Emphasis", "Data", "Summary", "Thank You"] = Field(
        ...,
        description="Type of the slide, selected from predefined slide categories"
    )
    content: str = Field(
        ...,
        description="Main textual content of the slide"
    )
    description: str | None = Field(
        None,
        description="Optional explanation or intent of the slide on 100-150 words"
    )


class Slides(BaseModel):
    slides: list[Slide] = Field(
        ...,
        description="Collection of slides forming the full presentation"
    )
