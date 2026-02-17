from typing import TypedDict, List, Optional
from pydantic import BaseModel, Field
from models.slide_data_models import Slides
from models.slide_layout_models import SlideLayout


class PresentationState(TypedDict):
    topic: str
    content: Optional[str]

    theme_info: Optional[str]
    
    slides:Optional[Slides]

    layout: Optional[SlideLayout]

    slide_content: Optional[List[str]]

    slides_code:Optional[List[str]]




