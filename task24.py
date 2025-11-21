from appZZ import Session
from modelZZ import User, user_association

session = Session()

user1 = User(name="Alice")
user2 = User(name="Bob")
user3 = User(name="Charlie")
user4 = User(name="Diana")

user1.following.append(user2)
user2.following.append(user1)
user1.following.append(user3)
user3.following.append(user1)
user2.following.append(user4)
user4.following.append(user2)

session.add_all([user1, user2, user3, user4])
session.commit()