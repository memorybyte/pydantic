from typing import List, Optional, Dict, Annotated
from pydantic import BaseModel, Field, EmailStr, AnyUrl, field_validator, model_validator, computed_field


class Address(BaseModel):
    city: str
    state: str
    pin: str


class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address
