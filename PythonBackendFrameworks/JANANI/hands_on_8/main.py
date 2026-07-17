from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db, engine
from models import Base, Course, Student, Enrollment
from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse,
    StudentCreate,
    EnrollmentCreate
)


app = FastAPI(
    title="Course Management API",
    description="College Course Management System API using FastAPI",
    version="1.0",
    contact={
        "name": "CTS Digital Nurture 5.0",
        "email": "support@cts.com"
    }
)



@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



@app.get(
    "/",
    tags=["Home"]
)
async def root():

    return {
        "message": "API running"
    }



# ================= COURSES =================


@app.get(
    "/api/courses/",
    tags=["Courses"],
    response_model=list[CourseResponse],
    summary="Get all courses"
)
async def get_courses(

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(
        select(Course)
    )

    return result.scalars().all()



@app.post(
    "/api/courses/",
    tags=["Courses"],
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create course"
)
async def create_course(

    course: CourseCreate,

    db: AsyncSession = Depends(get_db)

):

    new_course = Course(

        name=course.name,

        code=course.code,

        credits=course.credits,

        department_id=course.department_id
    )


    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)


    return new_course




@app.get(
    "/api/courses/{id}",
    tags=["Courses"],
    response_model=CourseResponse
)
async def get_course(

    id:int,

    db:AsyncSession=Depends(get_db)

):

    result = await db.execute(
        select(Course)
        .where(Course.id == id)
    )

    course = result.scalar_one_or_none()


    if course is None:

        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )


    return course




@app.put(
    "/api/courses/{id}",
    tags=["Courses"],
    response_model=CourseResponse
)
async def update_course(

    id:int,

    data:CourseUpdate,

    db:AsyncSession=Depends(get_db)

):

    result = await db.execute(
        select(Course)
        .where(Course.id == id)
    )


    course=result.scalar_one_or_none()


    if course is None:

        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )


    if data.name:
        course.name=data.name

    if data.code:
        course.code=data.code

    if data.credits:
        course.credits=data.credits


    await db.commit()

    await db.refresh(course)


    return course




@app.delete(
    "/api/courses/{id}",
    tags=["Courses"],
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_course(

    id:int,

    db:AsyncSession=Depends(get_db)

):

    result = await db.execute(
        select(Course)
        .where(Course.id == id)
    )


    course=result.scalar_one_or_none()


    if course is None:

        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )


    await db.delete(course)

    await db.commit()


    return None





# ================= STUDENTS =================


@app.post(
    "/api/students/",
    tags=["Students"],
    status_code=status.HTTP_201_CREATED
)
async def create_student(

    student:StudentCreate,

    db:AsyncSession=Depends(get_db)

):

    new_student=Student(

        name=student.name,

        email=student.email

    )


    db.add(new_student)

    await db.commit()

    await db.refresh(new_student)


    return new_student




@app.get(
    "/api/students/",
    tags=["Students"]
)
async def get_students(

    db:AsyncSession=Depends(get_db)

):

    result=await db.execute(
        select(Student)
    )

    return result.scalars().all()





# ================= ENROLLMENT =================


def send_confirmation_email(email:str):

    print(
        f"Sending confirmation to {email}"
    )



@app.post(
    "/api/enrollments/",
    tags=["Enrollments"],
    status_code=status.HTTP_201_CREATED
)
async def create_enrollment(

    enrollment:EnrollmentCreate,

    background_tasks:BackgroundTasks,

    db:AsyncSession=Depends(get_db)

):

    new_enrollment=Enrollment(

        student_id=enrollment.student_id,

        course_id=enrollment.course_id

    )


    db.add(new_enrollment)

    await db.commit()

    await db.refresh(new_enrollment)


    background_tasks.add_task(
        send_confirmation_email,
        "student@example.com"
    )


    return new_enrollment




@app.get(
    "/api/courses/{id}/students/",
    tags=["Courses"]
)
async def course_students(

    id:int,

    db:AsyncSession=Depends(get_db)

):

    result=await db.execute(

        select(Student)
        .join(
            Enrollment,
            Student.id == Enrollment.student_id
        )
        .where(
            Enrollment.course_id == id
        )

    )


    return result.scalars().all()