from modelXX import User, Address
from appXX import Session

session = Session()

user1 = User(name="Alice")
address1 = Address(email="alice@example.com", user=user1)

session.add(user1)
session.add(address1)
session.commit()