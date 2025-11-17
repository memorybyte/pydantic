from typing import List, Optional, Dict, Annotated
from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, model_validator, computed_field


class Patient(BaseModel):
    # name: str = Field(..., max_length=50, min_length=3)
    name: Annotated[str, Field(max_length=50, min_length=3, title='Name of the employee', description='Give the name of the patient in less than 50 characters', examples=[
                               'Memory Byte', 'GATE Overflow'])]  # Attaching metadata, useful for API docs
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    # weight: float = Field(..., gt=0)
    # Type coersion is overwritten
    weight: Annotated[float, Field(gt=0, strict=True)]
    # married: bool
    married: Annotated[bool, Field(
        default=None, description='Is the patient married or not')]
    # allergies: Optional[List[str]] = None
    # no more than 5 allergies
    allergies: Annotated[List[str], Field(max_length=5)]
    contact_details: Dict[str, str]


patient_info = {'name': 'Memory Byte', 'age': 20}

patient1 = Patient(**patient_info)
print(patient1)
