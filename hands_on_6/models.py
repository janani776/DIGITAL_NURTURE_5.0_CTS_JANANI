from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# ---------------- Department ----------------
class Department(Base):
    __tablename__ = 'departments'

    department_id = Column(Integer, primary_key=True, autoincrement=True)
    dept_name = Column(String(100))
    hod_name = Column(String(100))
    budget = Column(Integer)

    students = relationship("Student", back_populates="department")
    professors = relationship("Professor", back_populates="department")


# ---------------- Student ----------------
class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    enrollment_year = Column(Integer)

    department_id = Column(Integer, ForeignKey('departments.department_id'))

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")


# ---------------- Course ----------------
class Course(Base):
    __tablename__ = 'courses'

    course_id = Column(Integer, primary_key=True, autoincrement=True)
    course_name = Column(String(150))
    course_code = Column(String(20))

    enrollments = relationship("Enrollment", back_populates="course")


# ---------------- Enrollment ----------------
class Enrollment(Base):
    __tablename__ = 'enrollments'

    enrollment_id = Column(Integer, primary_key=True, autoincrement=True)

    student_id = Column(Integer, ForeignKey('students.student_id'))
    course_id = Column(Integer, ForeignKey('courses.course_id'))

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


# ---------------- Professor ----------------
class Professor(Base):
    __tablename__ = 'professors'

    professor_id = Column(Integer, primary_key=True, autoincrement=True)
    prof_name = Column(String(100))
    email = Column(String(100))
    salary = Column(Integer)

    department_id = Column(Integer, ForeignKey('departments.department_id'))

    department = relationship("Department", back_populates="professors")


# ---------------- DATABASE CONNECTION (MYSQL) ----------------
engine = create_engine(
    "mysql+mysqlconnector://root:@localhost:3306/college_db_orm",
    echo=True
)

Base.metadata.create_all(engine)