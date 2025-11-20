from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

class Base(DeclarativeBase):
    pass

class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

class User(BaseModel):
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)

    addresses: Mapped[list["Address"]] = relationship("Address", back_populates="user")

class Address(BaseModel):
    __tablename__ = "addresses"

    city: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    zip_code: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped["User"] = relationship("User", back_populates="addresses")