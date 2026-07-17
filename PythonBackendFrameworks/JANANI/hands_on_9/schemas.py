from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):

    email:EmailStr
    password:str



class UserLogin(BaseModel):

    email:EmailStr
    password:str



class CourseCreate(BaseModel):

    name:str
    code:str
    credits:int
    department_id:int