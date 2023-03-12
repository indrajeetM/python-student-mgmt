from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,IntegerField,SelectField
from wtforms.validators import DataRequired,Email,EqualTo,Length,NumberRange
from src.models import Division,Classes
class LoginForm(FlaskForm):

    email = StringField('Enter Email To Login',validators=[DataRequired(),Email()])
    password = PasswordField('Enter your Password',validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    all_divisions =[]# Division.query.order_by(Division.divname.asc())
    div_list = []
    if all_divisions:
        for item in all_divisions:
            div_list.append(tuple(item.id,item.divname))
    
    all_classess = []#Classes.query.order_by(Classes.classname.asc())
    class_list = []
    if all_classess:
        for item in all_classess:
            class_list.append(tuple(item.id,item.classname))

    first_name = StringField("Enter First Name ",validators=[DataRequired()])
    last_name = StringField("Enter Last Name",validators=[DataRequired()])
    gender = SelectField("Select Gender",validators=[DataRequired()],choices=[('Male','Male'),('Female','Female')])
    email = StringField('Enter Email Address',validators=[DataRequired(),Email()])
    mobile = IntegerField('Enter Mobile number',validators=[DataRequired(),NumberRange(min=1)])
    class_id = SelectField('Select Class',validators=[DataRequired()],choices=class_list)
    division_id = SelectField('Select Division',validators=[DataRequired()],choices=div_list)
    password = PasswordField('Enter your password',validators=[DataRequired(),EqualTo('confirm_password')])
    confirm_password = PasswordField('Enter Confirm Password',validators=[DataRequired()])
    submit = SubmitField('Register')

class AccountForm(FlaskForm):
    first_name = StringField("First Name ")
    last_name = StringField("Last Name")
    email = StringField('Email Address')
    mobile = IntegerField('Mobile number')


class HomeworkForm(FlaskForm):
    description = StringField("Enter the answer here ",validators=[DataRequired()])
    submit = SubmitField('Submit Anwer')