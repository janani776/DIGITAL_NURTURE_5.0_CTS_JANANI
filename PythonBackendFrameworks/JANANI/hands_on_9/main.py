from fastapi import (
    FastAPI,
    HTTPException,
    Depends,
    status
)

from fastapi.middleware.cors import CORSMiddleware

from fastapi.security import OAuth2PasswordBearer

from schemas import (
    UserCreate,
    UserLogin,
    CourseCreate
)

from models import (
    User,
    users,
    courses
)

from security import (
    get_password_hash,
    verify_password,
    create_access_token,
    decode_token
)



app=FastAPI(

    title="Secure Course Management API",
    version="1.0"
)



# CORS configuration

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:3000"
    ],

    allow_credentials=True,

    allow_methods=[
        "*"
    ],

    allow_headers=[
        "*"
    ]

)



oauth2_scheme = OAuth2PasswordBearer(

    tokenUrl="/api/v1/auth/login/"
)



# -------------------------
# Register User
# -------------------------


@app.post(
    "/api/v1/auth/register/"
)
def register(
    user:UserCreate
):

    for u in users:

        if u.email == user.email:

            raise HTTPException(

                status_code=409,

                detail="Email already registered"

            )


    new_user=User(

        id=len(users)+1,

        email=user.email,

        hashed_password=
        get_password_hash(
            user.password
        ),

        is_active=True
    )


    users.append(new_user)


    return {

        "message":
        "User registered successfully"

    }



# -------------------------
# Login JWT
# -------------------------


@app.post(
    "/api/v1/auth/login/"
)
def login(
    user:UserLogin
):


    existing=None


    for u in users:

        if u.email==user.email:

            existing=u



    if existing is None:

        raise HTTPException(

            status_code=401,

            detail="Invalid credentials"

        )


    if not verify_password(

        user.password,

        existing.hashed_password

    ):

        raise HTTPException(

            status_code=401,

            detail="Invalid credentials"

        )


    token=create_access_token(

        {
            "sub":
            existing.email
        }

    )


    return {

        "access_token":
        token,

        "token_type":
        "bearer"

    }



# -------------------------
# JWT Dependency
# -------------------------


def get_current_user(

    token:str=
    Depends(oauth2_scheme)

):


    payload=decode_token(token)


    if payload is None:

        raise HTTPException(

            status_code=401,

            detail="Invalid token"

        )


    email=payload.get("sub")


    for user in users:

        if user.email==email:

            return user



    raise HTTPException(

        status_code=401,

        detail="User not found"

    )



# -------------------------
# Protected Create Course
# -------------------------


@app.post(
    "/api/v1/courses/"
)
def create_course(

    course:CourseCreate,

    current_user:User=
    Depends(get_current_user)

):


    new_course={

        "id":
        len(courses)+1,

        **course.dict()

    }


    courses.append(new_course)


    return new_course




# -------------------------
# Protected Delete Course
# -------------------------


@app.delete(

"/api/v1/courses/{id}/"

)
def delete_course(

    id:int,

    current_user:User=
    Depends(get_current_user)

):


    for c in courses:


        if c["id"]==id:

            courses.remove(c)


            return {

                "message":
                "Deleted"

            }



    raise HTTPException(

        status_code=404,

        detail="Course not found"

    )



@app.get("/api/v1/courses/")
def get_courses():

    return courses



@app.get("/")
def root():

    return {

        "message":
        "Secure API Running"

    }



"""
OAuth2 Authorization Code Flow:

1. User logs into an Authorization Server.
2. Server returns an authorization code.
3. Client exchanges code for access token.
4. Client uses token to access resources.


JWT Login difference:

Simple JWT login directly accepts username/password
and returns a token.

OAuth2 Authorization Code flow uses a separate
authorization server and is safer for third-party apps.
"""