from modelX import User
from appX import Session

session = Session()

user1 = session.query(User).filter_by(id=2).first()

if user1:
    print(f"User id={user1.id}, name='{user1.name}'")
    print(f"Followers: {[f.id for f in user1.followers]}")
    print(f"Following: {[f.id for f in user1.following]}")