from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class SlideContent(BaseModel):
    slide_content: str = Field(
        ...,
        description="""The main textual content for the slide, extracted from the source material tailored to fit the slide's focus and type."  
         This content should be concise, relevant, and directly support the slide's purpose within the presentation.""")
    
