from modelX import User
from appX import Session

session = Session()

user1 = User(name="Alice Smith")
user2 = User(name="Bob Johnson")
user3 = User(name="Charlie Brown")

user1.following.append(user2)
user2.following.append(user3)

session.add_all([user1, user2, user3])
session.commit()