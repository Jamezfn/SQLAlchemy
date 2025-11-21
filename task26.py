from main import Session
from modelXY import User, Post

session = Session()

user = User(name="Alice Smith",
            posts=[Post(content="This is Alice's first post.")])

session.add(user)
session.commit()