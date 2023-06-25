import rain_orm
from rain_orm.column import Int, VarChar, DateTime


class Academy(rain_orm.Table):
    __table__ = "academies"
    __fields__ = {
        "id": Int(primary_key=True, auto_increment=True),
        "name": VarChar(30),
        "dean": VarChar(30)
    }


class Profession(rain_orm.Table):
    __table__ = "professions"
    __fields__ = {
        "id": Int(primary_key=True, auto_increment=True),
        "name": VarChar(30),
        "academy_id": Int(foreign_key=Academy.id)
    }


class Class(rain_orm.Table):
    __table__ = "classes"
    __fields__ = {
        "id": Int(primary_key=True, auto_increment=True),
        "size": Int(),
        "name": VarChar(30),
        "profession_id": Int(foreign_key=Profession.id)
    }


class Student(rain_orm.Table):
    __table__ = "students"
    __fields__ = {
        "id": Int(primary_key=True, auto_increment=True),
        "name": VarChar(20),
        "password": VarChar(500),
        "gender": VarChar(5),
        "birth": DateTime(),
        "origin": VarChar(30),
        "class_id": Int(foreign_key=Class.id)
    }


class Course(rain_orm.Table):
    __table__ = "courses"
    __fields__ = {
        "id": Int(primary_key=True, auto_increment=True),
        "name": VarChar(20),
        "start": Int(),
        "end": Int(),
        "day": Int()
    }

    
class Grade(rain_orm.Table):
    __table__ = "grades"
    __fields__ = {
        "id": Int(primary_key=True, auto_increment=True),
        "grade": Int(),
        "student_id": Int(foreign_key=Student.id),
        "course_id": Int(Course.id)
    }


class Admin(rain_orm.Table):
    __table__ = "admins"
    __fields__ = {
        "id": Int(primary_key=True, auto_increment=True),
        "name": VarChar(20),
        "password": VarChar(50)
    }


# view
class StudentInfo(rain_orm.Table):
    __table__ = "student_info"
    __fields__ = {
        "student_id": Int(),
        "student_name": VarChar(20),
        "gender": VarChar(5),
        "birth": DateTime(),
        "origin": VarChar(30),
        "class_name": VarChar(30),
        "profession_name": VarChar(30),
        "academy_name": VarChar(30)
    }


# view
class GradeInfo(rain_orm.Table):
    __table__ = "grade_info"
    __fields__ = {
        "grade": Int(),
        "student_id": Int(),
        "course_id": Int(),
        "course_name": VarChar(20),
        "student_name": VarChar(20),
        "class_name": VarChar(30),
        "profession_name": VarChar(30),
        "academy_name": VarChar(30)
    }


# view
class CourseInfo(rain_orm.Table):
    __table__ = "course_info"
    __fields__ = {
        "student_id": Int(),
        "course_id": Int(),
        "course_name": VarChar(20),
        "student_name": VarChar(20),
        "start": Int(),
        "end": Int(),
        "day": Int()
    }

