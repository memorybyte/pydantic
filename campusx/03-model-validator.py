from typing import List, Optional, Dict, Annotated
from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, model_validator, computed_field

# model validator: data validation depends on other field


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError(
                'Patients older than 60 must have an emergency contact')
        return model
