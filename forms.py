from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField

##WTForm
class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Please enter your email"), Email()])
    password = PasswordField("Password", validators=[DataRequired("Please enter your password.")])
    submit = SubmitField("Let Me In!")

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign Me Up!")
    