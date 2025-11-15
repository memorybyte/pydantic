from typing import List, Dict, Optional
from pydantic import BaseModel, Field, computed_field, field_validator, model_validator

# A model that refer another model
# A model that refer itself


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address  # Nested model referencing


class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None  # Self referencing model
    # Also, known as forward referencing


# When we use forward referencing, rebuild it
Comment.model_rebuild()


# Example
address = Address(
    street='Some street',
    city='There is a city',
    postal_code='123456'
)

user = User(
    id=1,
    name='Some name',
    address=address
)

# print(user.address.postal_code)

comment = Comment(
    id=1,
    content='This is a comment',
    replies=[
        Comment(
            id=2,
            content='Comment not found',
        )
    ]
)


# TODO:
# Create Course model
# Each Course has modules
# Each Module has Lessons

class Lesson(BaseModel):
    lesson_id: int
    topic: str


class Module(BaseModel):
    module_id: int
    name: str
    lessons: List[Lesson]


class Course(BaseModel):
    course_id: int
    name: str
    modules: List[Module]
