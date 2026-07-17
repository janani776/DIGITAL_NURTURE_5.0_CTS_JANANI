from flask import Flask, request, jsonify

app = Flask(__name__)

courses = [
    {
        "id":1,
        "name":"Python",
        "code":"CS101"
    },
    {
        "id":2,
        "name":"Java",
        "code":"CS102"
    }
]


@app.route("/api/courses/<int:id>", methods=["GET"])
def get_course(id):

    for course in courses:

        if course["id"] == id:
            return jsonify(course)


    return jsonify({
        "error":"Course not found"
    }),404



@app.route("/api/courses", methods=["GET"])
def get_courses():

    return jsonify(courses)



if __name__=="__main__":
    app.run(port=5001)