from typing import List, Optional, Dict, Annotated
from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, model_validator, computed_field

# Field validation is used for validating only one field
# Field validator operates in two modes: 'after' and 'before'
# Once the basic validation is completed, then field validation is performed
#


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def check_email(cls, v):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = v.split('@')[-1]
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return v

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
