from src import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash,generate_password_hash
from datetime import datetime


############### Models ###################

class Adminuser(db.Model,UserMixin):
    __tablename__ = 'adminusers'

    id = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(128))
    status = db.Column(db.Integer)

    def __init__(self,fname,email,password,status=0):
        self.fname = fname
        self.email = email
        self.password = generate_password_hash(password)
        self.status = status
    
    def check_password(self,password):
        return check_password_hash(self.password,password)
    

class Student(db.Model,UserMixin):

    __tablename__ = 'students'

    id = db.Column(db.Integer,primary_key=True)
    fname = db.Column(db.String(50))
    lname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    gender = db.Column(db.String(5))
    mobile = db.Column(db.String(50))
    password = db.Column(db.String(128))
    std_class = db.Column(db.String(20))
    std_div = db.Column(db.String(20))
    # stdclass = db.relationship('Classes',backref='stud_class',uselist=False)
    # stddiv = db.relationship('Division',backref='stud_div',uselist=False)
    # homework = db.relationship('Homework',backref='stud_homework',lazy='dynamic')

    def __init__(self,fname,lname,email,mobile,password,gender,std_class,std_div):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.mobile = mobile
        self.password = generate_password_hash(password)
        self.gender = gender
        self.std_class = std_class
        self.std_div = std_div

    def check_password(self,password):
        return check_password_hash(self.password,password)
    

class Classes(db.Model):

    __tablename__ = 'classes'

    id = db.Column(db.Integer,primary_key=True)
    classname = db.Column(db.String(10))
    # stdclass = db.relationship('ClassHomework',backref='class_name',uselist=False)
    def __init__(self,classname):
        self.classname = classname


class Division(db.Model):

    __tbalename__ = 'divisions'

    id = db.Column(db.Integer,primary_key=True)
    divname = db.Column(db.String(20))
    # stddiv = db.relationship('ClassHomework',backref='div_name',uselist=False)

    def __init__(self,divname):
        self.divname = divname


class ClassHomework(db.Model):

    __tablename__ = 'class_homeworks'

    id = db.Column(db.Integer,primary_key=True)
    subject = db.Column(db.String(50))
    description = db.Column(db.Text)
    last_date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    class_id = db.Column(db.Integer,db.ForeignKey('classes.id'))
    div_id = db.Column(db.Integer,db.ForeignKey('divisions.id'))

    def __init__(self,subject,description,last_date,class_id,div_id):
        self.subject = subject
        self.description = description
        self.last_date = last_date
        self.class_id = class_id
        self.div_id = div_id

class Homework(db.Model):

    __tablename__ = 'homeworks'

    id = db.Column(db.Integer,primary_key=True)
    homework_id = db.Column(db.Integer,db.ForeignKey('class_homeworks.id'))
    answer = db.Column(db.Text)
    submitted_date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    student_id = db.Column(db.Integer,db.ForeignKey('students.id'))

    def __init__(self,answer,std_id):
        self.answer = answer
        self.student_id = std_id

################# End Models ##################################

# class_1 = Classes('I')
# class_2 = Classes('II')
# class_3 = Classes('III')
# class_4 = Classes('IV')
# class_5 = Classes('V')
# class_6 = Classes('VI')
# class_7 = Classes('VII')
# class_8 = Classes('VIII')
# class_9 = Classes('IX')
# class_10 = Classes('X')

# class_a = Division('A')
# class_b = Division('B')
# class_c = Division('C')

# db.session.add([class_1,class_2,class_3,class_4,class_5,class_6,class_7,class_8,class_9,
# class_1,class_a,class_b,class_c])

# db.session.commit()

