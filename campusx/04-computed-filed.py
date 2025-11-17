from typing import List, Optional, Dict, Annotated
from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, model_validator, computed_field

# computed field: by using other field in the model, we create a new field


class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field()
    @property
    def bmi(self):
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi
