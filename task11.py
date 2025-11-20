from app import Session
from model import User
from app import Session
from sqlalchemy import or_

session = Session()

users = session.query(User).where(or_(User.age >= 30, User.name == "John Doe")).all()

for user in users:
    print(f"User {user.id}, name: {user.name}, age: {user.age}")