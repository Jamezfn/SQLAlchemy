from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model2 import Base

#postgresql_db_url = "postgresql+psycopg2://postgres:1234@localhost:5432/postgres"

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)

Base.metadata.create_all(engine)
