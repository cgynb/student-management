from flask import Blueprint, request, jsonify, g
from models.models import Student, StudentInfo, CourseInfo, GradeInfo
from utils.cryptographic import validate_password
from utils.authority import student_required

student_bp = Blueprint('student', __name__, url_prefix='/api/v1/student')


@student_bp.route("/login", methods=["POST"])
def student_login():
    args = dict(request.form)
    user = Student().where("id = ?", int(args.get("id"))).one()
    if user is not None and validate_password(args.get("password"), user.password):
        g.user = user
        g.role = "student"
        user = StudentInfo().where("student_id = ?", user.id).one()
        return jsonify({
            "code": 200,
            "message": "ok",
            "data": {
                "student": user.instance
            }
        })
    else:
        return jsonify({
            "code": 403,
            "message": "login fail",
            "data": None
        })


@student_bp.route("/courses", methods=["GET"])
@student_required
def get_courses():
    courses = CourseInfo().where("student_id = ?", g.user.id).all()
    courses = [item.instance for item in courses]
    return jsonify({
        "code": 200,
        "message": "ok",
        "data": {
            "courses": courses
        }
    })


@student_bp.route("/grades", methods=["GET"])
@student_required
def get_grades():
    grades = GradeInfo().where("student_id = ?", g.user.id).all()
    grades = [item.instance for item in grades]
    return jsonify({
        "code": 200,
        "message": "ok",
        "data": {
            "grades": grades
        }
    })
