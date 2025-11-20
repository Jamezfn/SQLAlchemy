from app import Session
from model import User
from app import Session

session = Session()

user = User(name="John Doe", age=30)

session.add(user)

session.commit()

users = session.query(User).all()

for user in users:
    print(f"User {user.id}, name: {user.name}, age: {user.age}")