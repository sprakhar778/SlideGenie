from pydantic import BaseModel, Field
from typing import List, Optional,Literal
THEMES = [
    "Obsidian Pro",
    "Midnight Galaxy",
    "Aurora Dark",
    "Ember Slate",
    "Forest Executive",
    "Ocean Depths",
    "Solar Flare",
    "Neon Cyberpunk",
    "Tropical Punch",
    "Crimson Noir",
    "Slate Steel",
    "Glacier Light",
    "Arctic Frost",
    "Modern Minimalist",
    "Rose Quartz",
]

class Theme(BaseModel):
    theme: Literal[*THEMES] = Field(description="The visual theme that best matches the tone and purpose of the presentation content.")