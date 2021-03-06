from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, SubmitField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    
class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=30)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6, max=50)])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Register")
