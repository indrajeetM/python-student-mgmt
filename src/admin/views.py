from flask import Flask,flash,Blueprint,redirect,url_for,render_template
from models import ClassHomework,Student,Adminuser,Homework
from src.admin.forms import *
from src import db

admin_views = Blueprint('admin',__name__)

@admin_views('/admin/login',methods=['GET','POST'])
def login():
    form = adminLoginForm()

    if form.validate_on_submit():
        email = form.email.data
        user = Adminuser.query.filter(email=email).first()
        if user:
            if user.check_password(form.password.data):
                return redirect(url_for('admin.dashboard'))
            else:
                flash('Invalid password')
                return redirect(url_for('admin.login'))
        else:
            flash('No user account found')
            return redirect(url_for('admin.login'))
    
    return render_template('common_login.html',form=form)

@admin_views.route('admin/dashboard')
def dashboard():
    total_students = Student.query.count()
    total_male = Student.query.filter_by(gender='Male').count()
    total_female = (total_students-total_male)
    return render_template('dashboard.html',
                           total_students=total_students,
                           total_male=total_male,
                           total_female=total_female)
    
@admin_views.route('/admin/add-class',methods=['GET','POST'])
def add_class():
    form = addClass()

    if form.validate_on_submit():
        className = form.classname.data
        isClassDuplicate = Classes.query.filter_by(classname=className)
        if isClassDuplicate:
            flash('Class Name Already Present')
            return redirect(url_for('admin.add_class'))
        else:
            newClass = Classes(classname=className)
            db.session.add(newClass)
            db.session.commit()
            flash('Class Added Successfully')
            return redirect(url_for('admin.add_class'))
    
    return render_template('add-class.html',form=form)
    
@admin_views.route('/admin/add-division',methods=['GET','POST'])
def add_division():
    form = addDivision()

    if form.validate_on_submit():
        divName = form.divisionname.data
        isDivDuplicate = Division.query.filter_by(divname=divName)
        if isDivDuplicate:
            flash('Division Name Already Present')
            return redirect(url_for('admin.add_division'))
        else:
            newClass = Division(divname=divName)
            db.session.add(newClass)
            db.session.commit()
            flash('Division Added Successfully')
            return redirect(url_for('admin.add_division'))
    
    return render_template('add-div.html',form=form)

@admin_views.route('/admin/add-homework')
def add_homework():

    form = addHomework()

    if form.validate_on_submit():
        class_id = form.classid.data
        div_id = form.divisionid.data
        subject = form.subject.data
        question = form.question.data
        last_date = form.lastdate.data

        newHomework = ClassHomework(subject=subject,
                                    description=question,
                                    last_date=last_date,
                                    class_id=class_id,
                                    div_id=div_id)
        db.session.add(newHomework)
        db.session.commit()
        flash('New Homework Added')
        return redirect(url_for('admin.view_homeworks'))
    
    return render_template('add-homework.html',form=form)

@admin_views.route('/admin/view-homeworks')
def view_homeworks():
    all_homework = ClassHomework.query.order_by(ClassHomework.id.desc())

    return render_template('all-homeworks.html',all_homework=all_homework)

@admin_views.route('/admin/view-homework-answers/<int:question_id>')
def view_homework_answers(question_id):
    all_homework = Homework.query.filter_by(homework_id=question_id).order_by(Homework.id.desc())

    return render_template('all-homework-answers.html',all_homework=all_homework)

