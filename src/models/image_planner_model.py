from pydantic import BaseModel,Field
from typing import List,Literal



class ImagePlan(BaseModel):
    image_keywords: str = Field(description="Short keyword tags for the image (3-6 words, comma-separated)")
    search_query: str = Field(description="Precise 8-15 word Unsplash search phrase, visual and concrete, optimized for photo search relevance")
    image_description: str = Field(description="Short description of where/how this image is used in the slide")
    
class ImagePlanList(BaseModel):
    image_plan_list:List[ImagePlan]=Field(description="List of image plans")    