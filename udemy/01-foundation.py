from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

# input_data = {'id': '1', 'name': 'mem', 'is_active': True}
# # user = User(input_data) # Error
# user = User(**input_data)
# print(user)

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product1  = Product(id=1, name='Laptop', price=999.99, in_stock=True)
product2 = Product(id=2, name='Mouse', price=24.33)
# product3 = Product(name='Kayboard') # Error, all mandatory field should be provided