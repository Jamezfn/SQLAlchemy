from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey, Table, Column, DateTime
from datetime import datetime, timezone

class Base(DeclarativeBase):
    pass

class BaseModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

class Appointment(BaseModel):
    __tablename__ = "appointments"

    doctor_id: Mapped[int] = mapped_column(Integer, ForeignKey("doctors.id"))
    patient_id: Mapped[int] = mapped_column(Integer, ForeignKey("patients.id"))
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    description: Mapped[str] = mapped_column(String(255))

    doctor: Mapped["Doctor"] = relationship("Doctor", back_populates="appointments", cascade="all, delete")
    patient: Mapped["Patient"] = relationship("Patient", back_populates="appointments", cascade="all, delete")


class Doctor(BaseModel):
    __tablename__ = "doctors"

    name: Mapped[str] = mapped_column(String(100))
    specialty: Mapped[str] = mapped_column(String(100))

    appointments: Mapped[list["Appointment"]] = relationship("Appointment", back_populates="doctor", cascade="all, delete")

class Patient(BaseModel):
    __tablename__ = "patients"

    name: Mapped[str] = mapped_column(String(100))
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String(10))

    appointments: Mapped[list["Appointment"]] = relationship("Appointment", back_populates="patient", cascade="all, delete")