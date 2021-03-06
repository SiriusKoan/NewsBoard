from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField, Recaptcha
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
    
class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=0, max=30, message="The name should be 4 to 30 letters long."), Regexp("[a-zA-Z0-9_-]+", message="Only letters, numbers and _- are allowed in username.")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=0, max=50, message="The password should be 6 to 50 letters long.")])
    repeat_password = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo('password', message="Passwords not match.")])
    email = EmailField("Email", validators=[DataRequired(), Email(message="Please type correct email format.")])
    language = SelectField("Language", choices=[("English", "English"), ("Chinese Tranditional", "Chinese Tranditional")], validators=[DataRequired()])
    recaptcha = RecaptchaField(validators=[Recaptcha(message="Please click 'I am not a robot.'")])
    submit = SubmitField("Register")
