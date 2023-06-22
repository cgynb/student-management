from flask import Flask, request, g
from flask_cors import CORS
import rain_orm
from utils.token import create_token, validate_token
from models.models import Student, Admin
from blueprints import student_bp, admin_bp

app = Flask(__name__)
app.register_blueprint(student_bp)
app.register_blueprint(admin_bp)
CORS(app, supports_credentials=True, expose_headers=['Authorization'], resources=r'/*')
rain_orm.connect(host="localhost", port=3306, user="root", password='123456', database="student_management")


@app.before_request
def before_request():
    user_id, role, msg = validate_token(request.headers.get('Authorization', "").replace("Bearer ", ""))
    user = None
    g.user = None
    if msg is None:
        try:
            if role == "student":
                user = Student().where("id = ?", user_id).one()
                g.role = "student"
            elif role == "admin":
                user = Admin().where("id = ?", user_id).one()
                g.role = "admin"
            g.user = user
        except Exception as e:
            print(e)


@app.after_request
def after_request(resp):
    if hasattr(g, 'user') and g.user is not None:
        resp.headers['Authorization'] = create_token(g.user.id, g.role)
    return resp


@app.route("/")
@app.route("/ping")
def ping():
    return "pong"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
