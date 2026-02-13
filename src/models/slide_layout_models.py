from pydantic import BaseModel, Field
from typing import List, Optional

class SlideLayout(BaseModel):
    layout_name: str = Field(..., description="The name of the slide layout (e.g., 'Split-Screen / Timeline')")
    rationale: str = Field(..., description="A brief 50-100 word  explanation of why this layout is suitable for the given topic and content type")
    components: List[str] = Field(..., description="A list of key components that make up the slide layout")