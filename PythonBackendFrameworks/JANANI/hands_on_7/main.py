from fastapi import FastAPI, HTTPException, status, Query
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel


app = FastAPI(
    title="Course Management API",
    description="RESTful Course Management API with Versioning, Pagination and Standard Error Handling",
    version="1.0.0",
    contact={
        "name": "Janani",
        "email": "janani@example.com"
    }
)


# -----------------------------
# Temporary Database
# -----------------------------

courses = [
    {
        "id": 1,
        "name": "Python",
        "code": "CS101",
        "credits": 4,
        "department_id": 1
    },
    {
        "id": 2,
        "name": "Java",
        "code": "CS102",
        "credits": 4,
        "department_id": 1
    },
    {
        "id": 3,
        "name": "Web Development",
        "code": "IT101",
        "credits": 3,
        "department_id": 2
    },
    {
        "id": 4,
        "name": "Database",
        "code": "IT102",
        "credits": 4,
        "department_id": 2
    }
]


# -----------------------------
# Schemas
# -----------------------------

class CourseCreate(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(CourseCreate):
    id: int



# -----------------------------
# Root
# -----------------------------

@app.get("/")
def root():
    return {
        "message": "API running"
    }



# -----------------------------
# GET ALL COURSES
# Versioned API + Pagination + Search
# -----------------------------

@app.get(
    "/api/v1/courses/",
    tags=["Courses"],
    response_description="Paginated course list"
)
def get_courses(
    page: int = 1,
    page_size: int = 2,
    search: Optional[str] = None
):

    result = courses


    # Search filter
    if search:
        result = [
            c for c in result
            if search.lower() in c["name"].lower()
            or search.lower() in c["code"].lower()
        ]


    total = len(result)


    start = (page - 1) * page_size
    end = start + page_size


    paginated = result[start:end]


    next_url = None
    previous_url = None


    if end < total:
        next_url = (
            f"/api/v1/courses/?page={page+1}"
            f"&page_size={page_size}"
        )


    if page > 1:
        previous_url = (
            f"/api/v1/courses/?page={page-1}"
            f"&page_size={page_size}"
        )


    return {
        "count": total,
        "next": next_url,
        "previous": previous_url,
        "results": paginated
    }



# -----------------------------
# GET SINGLE COURSE
# -----------------------------

@app.get(
    "/api/v1/courses/{course_id}/",
    response_model=CourseResponse,
    tags=["Courses"]
)
def get_course(course_id: int):

    for course in courses:
        if course["id"] == course_id:
            return course


    raise HTTPException(
        status_code=404,
        detail={
            "error":{
                "code":"NOT_FOUND",
                "message":
                f"Course with id {course_id} does not exist",
                "field":None
            }
        }
    )



# -----------------------------
# CREATE COURSE
# POST 201 + Location Header
# -----------------------------

@app.post(
    "/api/v1/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"]
)
def create_course(course: CourseCreate):

    new_course = {
        "id": len(courses)+1,
        **course.dict()
    }


    courses.append(new_course)


    response = JSONResponse(
        status_code=201,
        content=new_course
    )


    response.headers["Location"] = (
        f"/api/v1/courses/{new_course['id']}/"
    )


    return response



# -----------------------------
# PUT FULL UPDATE
# -----------------------------

@app.put(
    "/api/v1/courses/{course_id}/",
    response_model=CourseResponse,
    tags=["Courses"]
)
def update_course(
    course_id:int,
    course:CourseCreate
):

    for index,item in enumerate(courses):

        if item["id"] == course_id:

            updated = {
                "id":course_id,
                **course.dict()
            }

            courses[index]=updated

            return updated


    raise HTTPException(
        status_code=404,
        detail={
            "error":{
                "code":"NOT_FOUND",
                "message":
                f"Course with id {course_id} does not exist",
                "field":None
            }
        }
    )



# -----------------------------
# PATCH PARTIAL UPDATE
# -----------------------------

@app.patch(
    "/api/v1/courses/{course_id}/",
    response_model=CourseResponse,
    tags=["Courses"]
)
def patch_course(
    course_id:int,
    course:CourseUpdate
):

    for item in courses:

        if item["id"] == course_id:

            data = course.dict(exclude_none=True)

            item.update(data)

            return item


    raise HTTPException(
        status_code=404,
        detail={
            "error":{
                "code":"NOT_FOUND",
                "message":
                f"Course with id {course_id} does not exist",
                "field":None
            }
        }
    )



# -----------------------------
# DELETE COURSE
# 204 NO CONTENT
# -----------------------------

@app.delete(
    "/api/v1/courses/{course_id}/",
    status_code=204,
    tags=["Courses"]
)
def delete_course(course_id:int):

    for item in courses:

        if item["id"] == course_id:

            courses.remove(item)

            return None


    raise HTTPException(
        status_code=404,
        detail={
            "error":{
                "code":"NOT_FOUND",
                "message":
                f"Course with id {course_id} does not exist",
                "field":None
            }
        }
    )



# -----------------------------
# Versioning Note
# -----------------------------

"""
API Versioning Strategies:

1. URL Versioning:
   Example:
   /api/v1/courses/

   Advantages:
   - Simple
   - Easy to understand
   - Browser friendly


2. Header Based Versioning:
   Example:
   Accept:
   application/vnd.api+json;version=1

   Advantages:
   - Keeps URLs clean
   - Better for large APIs
"""