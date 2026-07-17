from flask import Blueprint, request, jsonify
from courses.extensions import db
from courses.models import Course, Student, Enrollment

courses_bp = Blueprint(
    "courses",
    __name__,
    url_prefix="/api/courses"
)


def make_response_json(data, status_code):
    return jsonify({
        "status": "success",
        "data": data
    }), status_code


@courses_bp.route("/", methods=["GET"])
def get_courses():

    courses = Course.query.all()

    return make_response_json(
        [course.to_dict() for course in courses],
        200
    )


@courses_bp.route("/", methods=["POST"])
def create_course():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    course = Course(
        name=data["name"],
        code=data["code"],
        credits=data["credits"],
        department_id=data["department_id"]
    )

    db.session.add(course)
    db.session.commit()

    return make_response_json(course.to_dict(), 201)


@courses_bp.route("/<int:id>/", methods=["GET"])
def get_course(id):

    course = Course.query.get_or_404(id)

    return make_response_json(course.to_dict(), 200)


@courses_bp.route("/<int:id>/", methods=["PUT"])
def update_course(id):

    course = Course.query.get_or_404(id)

    data = request.get_json()

    course.name = data.get("name", course.name)
    course.code = data.get("code", course.code)
    course.credits = data.get("credits", course.credits)
    course.department_id = data.get(
        "department_id",
        course.department_id
    )

    db.session.commit()

    return make_response_json(course.to_dict(), 200)


@courses_bp.route("/<int:id>/", methods=["DELETE"])
def delete_course(id):

    course = Course.query.get_or_404(id)

    db.session.delete(course)

    db.session.commit()

    return make_response_json(
        {"message": "Deleted Successfully"},
        200
    )


@courses_bp.route("/<int:id>/students/", methods=["GET"])
def course_students(id):

    course = Course.query.get_or_404(id)

    students = (
        Student.query
        .join(Enrollment)
        .filter(Enrollment.course_id == course.id)
        .all()
    )

    return make_response_json(
        [student.to_dict() for student in students],
        200
    )