from flask import Blueprint, request, jsonify, g
from models.models import Student, Admin, Academy, Profession, Class, Course, Grade, StudentInfo, CourseInfo, GradeInfo
from utils.cryptographic import generate_password, validate_password
from utils.authority import admin_required

admin_bp = Blueprint('admin', __name__, url_prefix='/api/v1/admin')


@admin_bp.route("/login", methods=["POST"])
def admin_login():
    args = dict(request.form)
    user = Admin().where("id = ?", args.get("id")).one()
    if user is not None and validate_password(args.get("password"), user.password):
        g.user = user
        g.role = "admin"
        return jsonify({
            "code": 200,
            "message": "ok",
            "data": {
                "admin": user.instance
            }
        })
    else:
        return jsonify({
            "code": 403,
            "message": "login fail",
            "data": None
        })


@admin_bp.route("/academy", methods=["POST"])
@admin_required
def add_academy():
    args = dict(request.form)
    academy = Academy(name=args.get("name"), dean=args.get("dean"))
    if academy.create():
        return jsonify({
            "code": 200,
            "message": "ok",
            "data": academy.instance
        })
    else:
        return jsonify({
            "code": 400,
            "message": "fail",
            "data": None
        })


@admin_bp.route("/academies", methods=["GET"])
@admin_required
def get_academies():
    academies = Academy().all()
    academies = [item.instance for item in academies]
    return jsonify({
        "code": 200,
        "message": "ok",
        "data": academies
    })


@admin_bp.route("/profession", methods=["POST"])
@admin_required
def add_profession():
    args = dict(request.form)
    profession = Profession(name=args.get("name"), academy_id=args.get("academy_id"))
    if profession.create():
        return jsonify({
            "code": 200,
            "message": "ok",
            "data": profession.instance
        })
    else:
        return jsonify({
            "code": 400,
            "message": "fail",
            "data": None
        })


@admin_bp.route("/professions", methods=["GET"])
@admin_required
def get_professions():
    professions = Profession().all()
    professions = [item.instance for item in professions]
    return jsonify({
        "code": 200,
        "message": "ok",
        "data": professions
    })


@admin_bp.route("/class", methods=["POST"])
@admin_required
def add_class():
    args = dict(request.form)
    class_ = Class(size=0, name=args.get("name"), profession_id=int(args.get("profession_id")))
    if class_.create():
        return jsonify({
            "code": 200,
            "message": "ok",
            "data": class_.instance
        })
    else:
        return jsonify({
            "code": 400,
            "message": "fail",
            "data": None
        })


@admin_bp.route("/classes", methods=["GET"])
@admin_required
def get_classes():
    classes = Class().all()
    classes = [item.instance for item in classes]
    return jsonify({
        "code": 200,
        "message": "ok",
        "data": classes
    })


@admin_bp.route("/student", methods=["POST"])
@admin_required
def add_student():
    args = dict(request.form)
    student = Student(name=args.get("name"), password=generate_password(args.get("password")),
                      gender=args.get("gender"), birth=args.get("birth"), origin=args.get("origin"),
                      class_id=args.get("class_id"))
    if student.create():
        return jsonify({
            "code": 200,
            "message": "ok",
            "data": student.instance
        })
    else:
        return jsonify({
            "code": 400,
            "message": "fail",
            "data": None
        })


@admin_bp.route("/students", methods=["GET"])
@admin_required
def get_students():
    students = StudentInfo().all()
    students = [item.instance for item in students]
    return jsonify({
        "code": 200,
        "message": "ok",
        "data": students
    })


@admin_bp.route("/student", methods=["PUT"])
@admin_required
def update_student():
    args = dict(request.form)
    student = Student().where("id=?", int(args.get("student_id"))).one()
    ok = student.update(args.get("set"), args.get("value"))
    if ok and student is not None:
        return jsonify({
            "code": 200,
            "message": "ok",
            "data": None
        })
    else:
        return jsonify({
            "code": 400,
            "message": "fail",
            "data": None
        })


@admin_bp.route("/course", methods=["POST"])
@admin_required
def add_course():
    args = dict(request.form)
    course = Course(name=args.get("name"), start=args.get("start"), end=args.get("end"), day=args.get("day"))
    if course.create():
        return jsonify({
            "code": 200,
            "message": "ok",
            "data": course.instance
        })
    else:
        return jsonify({
            "code": 400,
            "message": "fail",
            "data": None
        })


@admin_bp.route("/courses", methods=["GET"])
@admin_required
def admin_get_courses():
    courses = CourseInfo().all()
    courses = [item.instance for item in courses]
    return jsonify({
        "code": 200,
        "message": "ok",
        "data": courses
    })


@admin_bp.route("/grade", methods=["POST"])
@admin_required
def add_grade():
    args = dict(request.form)
    grade = Grade(student_id=args.get("student_id"), course_id=args.get("course_id"))
    if grade.create():
        return jsonify({
            "code": 200,
            "message": "ok",
            "data": grade.instance
        })
    else:
        return jsonify({
            "code": 400,
            "message": "fail",
            "data": None
        })


@admin_bp.route("/grade", methods=["PUT"])
@admin_required
def update_grade():
    args = dict(request.form)
    grade = Grade().where("student_id=?", args.get("student_id")).where("course_id=?", args.get("course_id"))
    ok = grade.update("grade", args.get("grade"))
    if ok:
        return jsonify({
            "code": 200,
            "message": "ok",
            "data": None
        })
    else:
        return jsonify({
            "code": 400,
            "message": "fail",
            "data": None
        })


@admin_bp.route("//grades")
@admin_required
def admin_get_grades():
    grades = GradeInfo().all()
    grades = [item.instance for item in grades]
    return jsonify({
        "code": 200,
        "message": "ok",
        "data": grades
    })
