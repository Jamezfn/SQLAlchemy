from app2 import Session
from model2 import User, Address
from app import Session

session = Session()

user1 = User(name="Alice", age=28)
user2 = User(name="Bob", age=35)
user3 = User(name="Charlie", age=42)
user4 = User(name="David", age=50)

address1 = Address(city="New York", state="NY", zip_code="10001")
address2 = Address(city="Los Angeles", state="CA", zip_code="90001")
address3 = Address(city="Chicago", state="IL", zip_code="60601")
address4 = Address(city="Houston", state="TX", zip_code="77001") 

user1.addresses.extend([address1, address3])
user2.addresses.append(address2)

session.add_all([user1, user2, user3, user4])
session.commit()

print(user1.addresses)
print(user2.addresses)
print(user3.addresses)
print(user4.addresses)