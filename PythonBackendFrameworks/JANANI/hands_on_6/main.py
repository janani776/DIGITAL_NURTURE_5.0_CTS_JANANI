from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from schemas import CourseCreate, CourseUpdate
from database import get_db, engine
from models import Base, Course


app = FastAPI(
    title="Course Management API",
    version="1.0"
)


# Create tables
@app.on_event("startup")
async def startup():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)



# Home route
@app.get("/")
async def root():

    return {
        "message": "API running"
    }



# GET all courses with pagination and filtering
@app.get("/api/courses/")
async def get_courses(

    skip: int = 0,

    limit: int = 10,

    department_id: int | None = None,

    db: AsyncSession = Depends(get_db)

):

    query = select(Course)


    if department_id:

        query = query.where(
            Course.department_id == department_id
        )


    query = query.offset(skip).limit(limit)


    result = await db.execute(query)


    courses = result.scalars().all()


    return courses




# GET course by id
@app.get("/api/courses/{course_id}")
async def get_course(

    course_id: int,

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(

        select(Course)
        .where(Course.id == course_id)

    )


    course = result.scalar_one_or_none()


    if course is None:

        return {
            "error": "Course not found"
        }


    return course




# POST create course
@app.post("/api/courses/")
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




# PUT update course
@app.put("/api/courses/{course_id}")
async def update_course(

    course_id: int,

    course_data: CourseUpdate,

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(

        select(Course)
        .where(Course.id == course_id)

    )


    course = result.scalar_one_or_none()


    if course is None:

        return {
            "error": "Course not found"
        }


    if course_data.name:

        course.name = course_data.name


    if course_data.code:

        course.code = course_data.code


    if course_data.credits:

        course.credits = course_data.credits


    await db.commit()


    await db.refresh(course)


    return course




# DELETE course
@app.delete("/api/courses/{course_id}")
async def delete_course(

    course_id: int,

    db: AsyncSession = Depends(get_db)

):

    result = await db.execute(

        select(Course)
        .where(Course.id == course_id)

    )


    course = result.scalar_one_or_none()


    if course is None:

        return {
            "error": "Course not found"
        }


    await db.delete(course)


    await db.commit()


    return {
        "message": "Course deleted successfully"
    }