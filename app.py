from flask import Flask, render_template, redirect, flash, url_for, request
from flask_cors import CORS
from flask_recaptcha import ReCaptcha
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    current_user,
    logout_user,
    login_required
)
import config
from db import db
from user_tools import login_auth, register
from os import listdir

app = Flask(__name__)
app.config.from_object(config.Config)
CORS(app)
recaptcha = ReCaptcha(app)
login_manager = LoginManager(app)
db.init_app(app)


class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(username):
    user = User()
    user.id = username
    return user

@app.before_first_request
def db_check():
    if 'data.db' not in listdir():
        db.create_all()


@app.route("/", methods=["GET", "POST"])
def index():
    if current_user.is_active:
        return redirect(url_for("dashboard_page"))
    else:
        # TODO
        return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login_page():
    if current_user.is_active:
        flash("You have logined.", category="info")
        return redirect(url_for("dashboard_page"))
    else:
        if request.method == "GET":
            return render_template("login.html")
        if request.method == "POST":
            username = request.form["username"]
            password = request.form["password"]
            if login_auth(username, password):
                user = User()
                user.id = username
                login_user(user)
                flash("Login as %s" % username, category="success")
                return redirect(url_for("dashboard_page"))
            else:
                flash("Login failed.", category="alert")
                return redirect(url_for("login_page"))


@app.route("/logout", methods=["GET"])
def logout_page():
    if current_user.is_active:
        logout_user()
        flash("Logout.", category="info")
        return redirect(url_for("index"))
    else:
        flash("You have not logined.", category="info")
        return redirect(url_for("login_page"))


@app.route("/register", methods=["GET", "POST"])
def register_page():
    if current_user.is_active:
        flash("You have logined.", category="info")
        return redirect(url_for("dashboard_page"))
    else:
        if request.method == "GET":
            return render_template("register.html")
        if request.method == "POST":
            if recaptcha.verify():
                username = request.form["username"]
                password = request.form["password"]
                email = request.form["email"]
                lang = request.form["language"]
                if register(username, password, email, lang):
                    flash("Register successfully.", category="success")
                    return redirect(url_for("login_page"))
                else:
                    flash("Bad characters or the username has been used.",
                          category="alert")
                    return redirect(url_for("register_page"))
            else:
                flash("Please click 'I am not a robot.'", category="alert")
                return redirect(url_for("register_page"))


@app.route("/dashboard", methods=["GET"])
def dashboard_page():
    if current_user.is_active:
        if request.method == "GET":
            # TODO
            return render_template("dashboard.html")
    else:
        flash("You have to login first.")
        return redirect(url_for("login_page"))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)
