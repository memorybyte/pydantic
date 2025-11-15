from typing import List, Dict, Optional
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


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
    address: Address  # Nested model referencing
    tags: List[str] = []

    # modify the formatting of datetime
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


# Create an instance
address = Address(
    street='street1',
    city='city1',
    zip_code='zipcode1'
)

user = User(
    id=1,
    name='name1',
    email='email1',
    is_active=True,
    created_at=datetime(2025, 10, 10, 14, 20),
    address=address,
    tags=['premium', 'subscriber']
)

print(user.created_at)


# model_dump(): returns a dictionary representation of the model's field
# model_dump_json(): returns a JSON string representation of model_dump()

# using model_dump()
python_dict = user.model_dump()
print(python_dict)

# using model_dump_json()
json_str = user.model_dump_json()  # it is a string
print(f'\n\n{json_str}')
