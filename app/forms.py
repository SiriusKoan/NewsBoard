from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, ValidationError


class LoginForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired()], render_kw={"placeholder": "Username"}
    )
    password = PasswordField(
        "Password", validators=[DataRequired()], render_kw={"placeholder": "Password"}
    )
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=4, max=30, message="The name should be 4 to 30 letters long."),
            Regexp(
                "[a-zA-Z0-9_-]+",
                message="Only letters, numbers and _- are allowed in username.",
            ),
        ],
        render_kw={"placeholder": "Username"},
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(
                min=6, max=50, message="The password should be 6 to 50 letters long."
            ),
        ],
        render_kw={"placeholder": "Password"},
    )
    repeat_password = PasswordField(
        "Repeat Password",
        validators=[
            DataRequired(),
            EqualTo("password", message="Passwords not match."),
        ],
        render_kw={"placeholder": "Repeat Password"},
    )
    email = EmailField(
        "Email", validators=[DataRequired()], render_kw={"placeholder": "Email"}
    )
    language = SelectField(
        "Language: ",
        choices=[("en", "English")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Register")


class UserSettingForm(FlaskForm):
    password = PasswordField(
        "Password",
        render_kw={"placeholder": "Password"},
    )
    email = EmailField(
        "Email", validators=[DataRequired()], render_kw={"placeholder": "Email"}
    )
    language = SelectField(
        "Language: ",
        choices=[("en", "English")],
        validators=[DataRequired()],
    )
    submit = SubmitField("Update")

    def validate_password(self, field):
        if type(field.data) is str:
            if field.data != "" and (len(field.data) < 6 or len(field.data) > 50):
                raise ValidationError("The password should be 6 to 50 letters long.")
        else:
            raise ValidationError("Invalid.")
