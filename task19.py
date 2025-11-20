from modelXX import User
from appXX import Session

session = Session()

users = session.query(User).all()
for user in users:
    print(f"User {user.id}, name: {user.name}")
    for address in user.addresses:
        print(f"Email: {address.email}")