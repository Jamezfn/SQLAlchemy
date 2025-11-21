from appZZ import Session
from modelZZ import User, user_association

session = Session()

user = session.query(User).where(User.id == 1).one_or_none()
if user is None:
    print("User not found.")
    exit()

print(f"User {user.id}, name: {user.name}")
print("Following:")
for followed in user.following:
    print(f"- User {followed.id}, name: {followed.name}")
print("Followers:")
for follower in user.followers:
    print(f"- User {follower.id}, name: {follower.name}")