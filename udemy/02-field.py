from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import re

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]


class Blog(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None

cart_data = {
    'user_id': 12,
    'items': ['laptop', 'mouse', 'keyboard'],
    'quantities': {'laptop': 1, 'mouse': 2, 'keyboard': 3}
}

# print(cart_data)

class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., # makes it required field
        min_length=3,
        max_length=50,
        description='Employee name',
        # examples='Memory Byte',
        examples=['Memory Byte'],
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ..., # makes it required field
        ge=10000,
        le=1000000,
        description='Annual salary in USD'
    )

# print(Employee(id=1, name='Memory Byte'))

class User(BaseModel):
    email: str = Field(..., regex=r'')
    phone: str = Field(..., regex='')
    age: int = Field(..., ge=0, lt=150, description='Age of user in years')
    discount: float = Field(..., ge=0, le=100, description='Discount percentage')