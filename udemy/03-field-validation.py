from pydantic import BaseModel, field_validator, model_validator

# Field() validate the field in the class.
# For additional customized validation, field_validator has to be used.
# This is only for one field.
# Ex: @field_validator('field_name') -> it is a decorator
#     def username_length():
#

# model validator: runs in a mode
# 

class User(BaseModel):
    username: str


    @field_validator('username')
    def username_length(cls, value):
        if len(value) < 4:
            raise ValueError('Username must be at least 4 characters')
        return value
    
class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Password does not match')
        return values

    