from sqlalchemy.orm import sessionmaker
from models import engine, Department, Student, Course, Enrollment, Professor

Session = sessionmaker(bind=engine)
session = Session()

# ---------------- INSERT ----------------

d1 = Department(dept_name="Computer Science", hod_name="Dr. Ramesh", budget=850000)
d2 = Department(dept_name="Electronics", hod_name="Dr. Priya", budget=600000)

session.add_all([d1, d2])
session.commit()

s1 = Student(first_name="Arjun", last_name="Mehta", email="arjun@college.edu", enrollment_year=2022, department_id=1)
s2 = Student(first_name="Priya", last_name="Suresh", email="priya@college.edu", enrollment_year=2022, department_id=1)

session.add_all([s1, s2])
session.commit()

c1 = Course(course_name="DBMS", course_code="CS101")
c2 = Course(course_name="DSA", course_code="CS102")

session.add_all([c1, c2])
session.commit()

e1 = Enrollment(student_id=1, course_id=1)
e2 = Enrollment(student_id=1, course_id=2)
e3 = Enrollment(student_id=2, course_id=1)

session.add_all([e1, e2, e3])
session.commit()

# ---------------- READ ----------------

print("\nSTUDENTS LIST:")
students = session.query(Student).all()
for s in students:
    print(s.first_name, s.last_name)

print("\nENROLLMENTS:")
enrollments = session.query(Enrollment).all()
for e in enrollments:
    print(e.student_id, e.course_id)

# ---------------- UPDATE ----------------

student = session.query(Student).filter_by(email="arjun@college.edu").first()
student.enrollment_year = 2023
session.commit()

# ---------------- DELETE ----------------

enroll = session.query(Enrollment).first()
session.delete(enroll)
session.commit()

print("\nDONE SUCCESSFULLY")