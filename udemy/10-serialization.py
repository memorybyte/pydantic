from typing import Dict, List, Optional
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime

# Serialization: process of converting complex data structure (complex pydantic model) into easily stored, processed structure (JSON strings, python dict)

class Address(BaseModel):
    street: str
    city: str
    zip_code: str


class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: Optional[List[str]] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


user = User(
    id=1,
    name='Memory Byte',
    email='memorybyte@email.com',
    created_at=datetime(2025, 10, 13, 14, 30),
    address=Address(
        street='s1',
        city='c1',
        zip_code='z1'
    ),
    is_active=False,
    tags=['premium', 'subscriber']
)
print(user)
print('='*50)
python_dict = user.model_dump()
print(python_dict)
print('='*50)
json_string = user.model_dump_json()
print(json_string)