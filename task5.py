from app import Session
from model import User
from app import Session

session = Session()

user = session.query(User).filter_by(id=1).first()

session.delete(user)

session.commit()