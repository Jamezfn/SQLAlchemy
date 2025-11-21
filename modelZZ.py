from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Table, Column
from typing import List

class Base(DeclarativeBase):
    pass

user_association = Table(
    "user_association",
    Base.metadata,
    Column("follower_id", Integer, ForeignKey("users.id"), primary_key=True),
    Column("followed_id", Integer, ForeignKey("users.id"), primary_key=True),
)

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)

    following: Mapped[List["User"]] = relationship(
        "User",
        secondary=user_association,
        primaryjoin=id == user_association.c.follower_id,
        secondaryjoin=id == user_association.c.followed_id,
        back_populates="followers",
    )

    followers: Mapped[List["User"]] = relationship(
        "User",
        secondary=user_association,
        primaryjoin=id == user_association.c.followed_id,
        secondaryjoin=id == user_association.c.follower_id,
        back_populates="following",
    )