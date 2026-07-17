from pydantic import BaseModel


class User(BaseModel):

    id:int
    email:str
    hashed_password:str
    is_active:bool=True



users=[]


class Course(BaseModel):

    id:int
    name:str
    code:str
    credits:int
    department_id:int


courses=[
    {
        "id":1,
        "name":"Python",
        "code":"CS101",
        "credits":4,
        "department_id":1
    }
]