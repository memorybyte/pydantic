from typing import List, Dict, Optional
from pydantic import BaseModel, Field, field_validator, model_validator, computed_field

# Customized validation -> use field_validator decorator
#


class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        # This function takes 2 parameter: one is class and other is value
        if len(v) < 4:
            raise ValueError('Username must be at least 4 characters')
        return v


class SignupData(BaseModel):
    password: str
    confirm_password: str

    # 'after' means all validation is performed, them this validation will take place
    @model_validator(mode='after')
    def password_catch(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password do not match')
        return values


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field  # a new property is made and can be accessed
    @property
    def total_price(self) -> float:
        return self.price * self.quantity


class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rates_per_night: float

    @computed_field(mode='after')
    @property
    def total_amount(self) -> float:
        return self.nights * self.rates_per_night
