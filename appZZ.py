from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modelZZ import Base, User, user_association

#postgresql_db_url = "postgresql+psycopg2://postgres:1234@localhost:5432/postgres"
db_url = "sqlite:///database.db"

engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)