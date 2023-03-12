from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,TextAreaField,DateField
from wtforms.validators import DataRequired
from src.models import Classes,Division
from datetime import date

class adminLoginForm(FlaskForm):
    
    email = StringField('Enter Your email',validators=[DataRequired()])
    password = PasswordField('Enter Your password',validators=[DataRequired()])
    submit = SubmitField('Login')

class addClass(FlaskForm):

    classname = StringField('Enter Class Name',validators=[DataRequired()])
    submit = SubmitField('Save Class')

class updateClass(FlaskForm):

    classname = StringField('Enter Class Name',validators=[DataRequired()])
    submit = SubmitField('Update Class')

class addDivision(FlaskForm):

    divisionname = StringField('Enter Division Name',validators=[DataRequired()])
    submit = SubmitField('Save Division')


class updateDivision(FlaskForm):

    divisionname = StringField('Enter Division Name',validators=[DataRequired()])
    submit = SubmitField('Update Division')

class addHomework(FlaskForm):
    all_classes = []#Classes.query.order_by(Classes.classname.asc())
    class_list = []
    if all_classes:
        for clas in all_classes:
            class_list.append((clas.id,clas.classname))

    all_division = []#Division.query.order_by(Division.divname.asc())
    classid = SelectField('Select Class',validators=[DataRequired()],
                          choices=class_list)
    div_list = []
    if all_division:
        for div in all_division:
            div_list.append((div.id,div.divname))

    divisionid = SelectField('Select Division',validators=[DataRequired()],
                          choices=div_list)
    subject = StringField('Enter Subject Title',validators=[DataRequired])
    question = TextAreaField('Enter Question Details Here',validators=[DataRequired])
    lastdate = DateField('Last Date to submit',validators=[DataRequired()],default=date.today)



