from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Table, Column

class Base(DeclarativeBase):
    pass

student_cause = Table(
    "student_cause",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id"), primary_key=True),
    Column("cause_id", Integer, ForeignKey("causes.id"), primary_key=True)
)

class Student(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    causes: Mapped[list["Cause"]] = relationship("Cause",
                                                secondary=student_cause, 
                                                 back_populates="students")

class Cause(Base):
    __tablename__ = "causes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String(100))
    students: Mapped["Student"] = relationship("Student", 
                                               secondary=student_cause,
                                               back_populates="causes")