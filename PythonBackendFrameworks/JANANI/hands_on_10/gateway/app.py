from flask import Flask,request
import requests


app=Flask(__name__)


COURSE_SERVICE="http://localhost:5001"
STUDENT_SERVICE="http://localhost:5002"



@app.route(
"/api/courses/<path:path>",
methods=["GET"]
)
def courses(path):

    response=requests.request(

        method=request.method,

        url=f"{COURSE_SERVICE}/api/courses/{path}",

        json=request.json

    )

    return response.json(),response.status_code



@app.route(
"/api/students/<path:path>",
methods=["POST"]
)
def students(path):

    response=requests.request(

        method=request.method,

        url=f"{STUDENT_SERVICE}/api/students/{path}",

        json=request.json

    )


    return response.json(),response.status_code



if __name__=="__main__":

    app.run(port=5000)