from pydantic import BaseModel, Field
from typing import List, Optional, Literal




class Slide_Type(BaseModel):
    slide_type: Literal["Hero", "Agenda", "Key Points", "Concept Explanation", "Process", "Comparison", "Visual Emphasis", "Data", "Summary", "Thank You"] = Field(
        ...,
        description="Type of the slide, selected from predefined slide categories"
    )
    description:str =Field(
        ...,
        description="Brief explanation of content that will be presented here in the presentation")

class Slides_Types(BaseModel):
    slide_types: list[Slide_Type] = Field(
        ...,
        description="Collection of slides forming the full presentation"
    )
   