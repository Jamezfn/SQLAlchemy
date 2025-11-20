from app import Session
from model import User
from app import Session

session = Session()

user = session.query(User).filter_by(id=1).one_or_none()

user.name = "Jane Doe"
user.age = 31

session.commit()