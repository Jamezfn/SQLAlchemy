from main import Session
from modelXY import User, Post

session = Session()

posts = session.query(Post).all()
for post in posts:
    print(f"Post {post.id}, content: {post.content}, user_id: {post.user_id}")

user = session.query(User).where(User.id == 1).one_or_none()
print(f"User {user.id}, name: {user.name}")