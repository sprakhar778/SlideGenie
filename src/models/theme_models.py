from pydantic import BaseModel, Field
from typing import List, Optional,Literal

class Theme(BaseModel):
    theme: Literal[
        "Ocean Depths", 
        "Sunset Boulevard", 
        "Forest Canopy", 
        "Modern Minimalist", 
        "Golden Hour", 
        "Arctic Frost", 
        "Desert Rose", 
        "Tech Innovation", 
        "Botanical Garden", 
        "Midnight Galaxy"
    ] = Field(description="The visual theme that best matches the tone and purpose of the presentation content.")