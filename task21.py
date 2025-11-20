from modelYY import Student, Cause
from appYY import Session

session = Session()

s = Student(name="Jane")
c1 = Cause(description="Tree planting")
c2 = Cause(description="Beach cleanup")

s.causes.append(c1)
s.causes.append(c2)

session.add(s)
session.commit()
