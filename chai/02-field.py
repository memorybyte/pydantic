from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description='Employee Name',
        example='Memory Byte'
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000
    )
