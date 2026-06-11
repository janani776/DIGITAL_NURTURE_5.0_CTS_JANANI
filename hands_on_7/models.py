from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"
    department_id = Column(Integer, primary_key=True)
    dept_name = Column(String(100))
    hod_name = Column(String(100))
    budget = Column(Integer)

class Student(Base):
    __tablename__ = "students"
    student_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(100))
    enrollment_year = Column(Integer)

    # REQUIRED FOR HANDS-ON 7
    is_active = Column(Boolean, default=True)

    department_id = Column(Integer, ForeignKey("departments.department_id"))

class Course(Base):
    __tablename__ = "courses"
    course_id = Column(Integer, primary_key=True)
    course_name = Column(String(150))
    course_code = Column(String(20))

class CourseSchedule(Base):
    __tablename__ = "course_schedules"
    schedule_id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("courses.course_id"))
    day_of_week = Column(String(20))
    start_time = Column(String(20))
    end_time = Column(String(20))