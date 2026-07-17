from flask import Flask,request,jsonify
import requests


app=Flask(__name__)


students=[
    {
        "id":1,
        "name":"Janani"
    }
]


@app.route("/api/students/<int:id>/enroll",
methods=["POST"])
def enroll(id):

    data=request.json

    course_id=data["course_id"]


    try:

        response=requests.get(
            f"http://localhost:5001/api/courses/{course_id}"
        )


    except requests.exceptions.ConnectionError:

        return jsonify({

            "error":
            "Course Service unavailable"

        }),503



    if response.status_code!=200:

        return jsonify({

            "error":
            "Invalid course"

        }),404



    return jsonify({

        "message":
        "Student enrolled successfully",

        "student_id":
        id,

        "course":
        response.json()

    })



if __name__=="__main__":

    app.run(port=5002)