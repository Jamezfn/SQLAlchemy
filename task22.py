from appY import Session
from modelZ import Doctor, Patient, Appointment

session = Session()

doc1 = Doctor(name="Dr. Smith", specialty="Cardiology")
doc2 = Doctor(name="Dr. Adams", specialty="Neurology")

pat1 = Patient(name="Alice Johnson", age=45, gender="Female")
pat2 = Patient(name="Bob Brown", age=50, gender="Male")

appt1 = Appointment(doctor=doc1, patient=pat1, description="Regular check-up")
appt2 = Appointment(doctor=doc2, patient=pat1, description="Neurology consultation")
appt3 = Appointment(doctor=doc1, patient=pat2, description="Cardiology follow-up")

session.add_all([doc1, doc2, pat1, pat2, appt1, appt2, appt3])
session.commit()