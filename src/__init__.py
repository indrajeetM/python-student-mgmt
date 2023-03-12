from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager,UserMixin
from werkzeug.security import check_password_hash,generate_password_hash
from datetime import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = 'MYSECRETKEY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/student_mgmt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()
Migrate(app,db)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'student.login'



# @login_manager.user_loader
# def load_user(user_id):
#     return Adminuser.query.get(user_id)

################## Blueprints #################
from src.core.views import core
from src.student.views import students
app.register_blueprint(core)
app.register_blueprint(students)