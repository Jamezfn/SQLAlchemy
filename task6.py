from app import Session
from model import User
from app import Session

session = Session()

users = session.query(User).order_by(User.age).all()

for user in users:
    print(f"User {user.id}, name: {user.name}, age: {user.age}")