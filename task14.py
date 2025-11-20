from app import Session
from model import User
from app import Session
from sqlalchemy import func

session = Session()

users_tuple = (
    session.query(User, func.count(User.id))
    .filter(User.age >= 30)
    .order_by(User.age)
    .filter(User.age <= 50)
    .group_by(User.age)
    .all()
)
for user, count in users_tuple:
    print(f"age: {user.age}, count: {count}")