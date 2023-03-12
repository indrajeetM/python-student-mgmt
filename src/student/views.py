from flask import render_template,Blueprint,url_for,redirect,request,flash
from flask_login import login_user,logout_user,current_user,login_required
from src.student.forms import LoginForm,RegisterForm,AccountForm,HomeworkForm
from src import db
from src.models import *
from werkzeug.security import check_password_hash,generate_password_hash


students = Blueprint('student',__name__)

@students.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit() and form.validate():
        fname = form.first_name.data
        lname = form.last_name.data
        email = form.email.data
        mobile = form.mobile.data
        gender = form.gender.data
        password = form.password.data
        class_id = form.class_id.data
        division_id = form.division_id.data
        
        newstudent = Student(fname=fname,
                lname=lname,
                email=email,
                mobile=mobile,
                password=password,
                gender=gender,
                std_class=class_id,
                std_div=division_id
                )
        db.session.add(newstudent)
        db.seesion.commit()
        return redirect(url_for('core.index'))
    
    
    return render_template('student_register.html',form=form)

@students.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    routes = url_for('student.login')

    if form.validate_on_submit() and form.validate():
        student = Student.query.filter_by(email=form.email.data).first()
        if student.check_password(form.password.data) and student is not None:
            login_user(student)
            flash('Login success')

            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('common_login.html',route=routes,form=form)

@students.route('/logout',methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('core.index'))

@students.route('/account',methods=['GET','POST'])
@login_required
def account():
    form = AccountForm()

    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.email.data = current_user.email
    form.mobile.data = current_user.mobile

    return render_template('account.html',form=form)


@students.route('/homework',methods=['GET','POST'])
@login_required
def list_homeworks():
    
    page = request.args.get('page',1,type=int)
    homeWorkList = ClassHomework.query.filter_by(class_id=current_user.stdclass,div_id=current_user.stddiv).order_by(ClassHomework.id.desc()).paginate(page=page,per_page=5)
    return render_template('homework_listing.html',homeWorkList=homeWorkList)


@students.route('/homework/<int:homework_id>',methods=['GET','POST'])
@login_required
def homework(homework_id):
    classHomework = ClassHomework.query.get_or_404(homework_id)
    form = HomeworkForm()
    answer = Homework.query.filter_by(homework_id=homework_id).first()
    if answer:
        if form.validate_on_submit():
            answer.answer=form.description.data
            db.session.commit()
            return redirect(url_for('student.homework'))
        
        form.description.data = answer.answer
    elif form.validate_on_submit():
        answer = form.description.data
        homework = Homework(answer=answer,std_id=current_user.id)
        db.session.add(homework)
        db.session.commit()
        return redirect(url_for('student.homework'))
    
    return render_template('homework_answer.html',form=form,question=classHomework)
