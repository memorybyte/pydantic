from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    is_active: bool


input_data = {'id': 101, 'name': 'ChaiCode', 'is_active': True}

# user = User(**input_data)
# print(user, type(user))


class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: int = True


print(Product)
print(type(Product))
