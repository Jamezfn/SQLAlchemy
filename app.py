from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

#postgresql_db_url = "postgresql+psycopg2://postgres:1234@localhost:5432/postgres"

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

user = User(name="John Doe", age=30)

session.add(user)

session.commit()
