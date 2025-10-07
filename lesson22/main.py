from pydantic import BaseModel

# class User(BaseModel):
#     id: int
#     name: str
#     email: str


# user = User(id=1, name="John Doe", email="john.doe@exaple.com")
# print(user)    


class User(BaseModel):
    id: int
    name: str
    age: int = 0
    email: str = "example@example.com"

user1 = User(id=1, name="John Doe", age=30, email="john.doe@example.com")    
print(user1)
user2 = User(id=2, name="John Doe", age=30)    
print(user2)
user3 = User(id=3, name="John Doe")    
print(user3)