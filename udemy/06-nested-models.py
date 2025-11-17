from typing import List, Dict, Optional, Literal
from pydantic import BaseModel, Field, model_validator, field_validator

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street='street1',
    city='city1',
    postal_code='123456'
)

user = User(
    id=1,
    name='name1',
    address=address
)

user_data = {
    'id': 1,
    'name': 'name1',
    'address': {'street': 's1', 'city': 'c1', 'postal_code': 'p1'}
}

user = User(**user_data)