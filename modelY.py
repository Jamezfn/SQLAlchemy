from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

class Base(DeclarativeBase):
    pass

class Node(Base):
    __tablename__ = "nodes"

    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    value : Mapped[str] = mapped_column(Integer, nullable=False)
    next_id : Mapped[int | None] = mapped_column(ForeignKey("nodes.id"), nullable=True)
    next_node : Mapped["Node | None"] = relationship("Node", back_populates="previous_node", remote_side=[id])
    previous_node : Mapped["Node | None"] = relationship("Node", back_populates="next_node", uselist=False)