from flask_login import (
    login_user,
    current_user,
    logout_user,
    login_required,
)
from flask_recaptcha import ReCaptcha
from flask import current_app, request, render_template, flash, redirect, url_for
from .user_tools import login_auth, register
from . import user_bp
from ..db import db


@user_bp.route("/login", methods=["GET", "POST"])
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
                return redirect(url_for("user.login_page"))


@user_bp.route("/logout", methods=["GET"])
@login_required
def logout_page():
    logout_user()
    flash("Logout.", category="info")
    return redirect(url_for("index"))


@user_bp.route("/register", methods=["GET", "POST"])
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
                    return redirect(url_for("user.login_page"))
                else:
                    flash("Bad characters or the username has been used.",
                          category="alert")
                    return redirect(url_for("user.register_page"))
            else:
                flash("Please click 'I am not a robot.'", category="alert")
                return redirect(url_for("user.register_page"))
