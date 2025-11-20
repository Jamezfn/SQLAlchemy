from app import Session
from model import User
from app import Session
from sqlalchemy import func

session = Session()

users = session.query(User, func.count(User.id)).group_by(User.age).all()

for user, count in users:
    print(f"age: {user.age}, count: {count}")