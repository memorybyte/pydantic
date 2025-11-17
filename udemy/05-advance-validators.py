from pydantic import BaseModel, Field, computed_field, field_validator, model_validator
from typing import List, Dict, Annotated, Optional
from datetime import datetime

# Multiple Field Validation
class Person(BaseModel):
    first_name: str
    last_name: str

    # Multiple field validation
    @field_validator('first_name', 'last_name') # same validation check performed on these fields
    def names_must_be_capitalized(cls, v):
        if not v.istitle():
            raise ValueError('Names must be capitalized ')
        return v
    
# Data Transformation Patterm
class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, v):
        return v.strip().lower()
    


class Product(BaseModel):
    price: str # Example: $4.44

    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', '').replace(',', ''))
        return v
    
class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after')
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError('End date must be after start date')
        return values