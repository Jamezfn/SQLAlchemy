from appY import Session
from modelZ import Doctor, Patient, Appointment

session = Session()

appts = session.query(Appointment).all()
appts2 = session.query(Appointment).filter(Appointment.patient.has(name="Alice Johnson")).all()

for appt in appts2:
    print(f"[Filtered] Appointment ID: {appt.id}, Doctor: {appt.doctor.name}, Patient: {appt.patient.name}, Date: {appt.date}, Description: {appt.description}")

for appt in appts:
    print(f"Appointment ID: {appt.id}, Doctor: {appt.doctor.name}, Patient: {appt.patient.name}, Date: {appt.date}, Description: {appt.description}")