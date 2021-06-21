from flask_login import (
    login_user,
    current_user,
    logout_user,
    login_required,
)
from flask import request, render_template, flash, redirect, url_for
from ..user_tools import login_auth, register, render_user_data, update_user
from . import user_bp
from ..forms import LoginForm, RegisterForm, UserSettingForm


@user_bp.route("/login", methods=["GET", "POST"])
def login_page():
    if current_user.is_active:
        flash("You have logined.", category="info")
        return redirect(url_for("dashboard.dashboard_page"))
    else:
        form = LoginForm()
        if request.method == "GET":
            return render_template("login.html", form=form)
        if request.method == "POST":
            if form.validate_on_submit():
                username = form.username.data
                password = form.password.data
                if user := login_auth(username, password):
                    login_user(user, remember=True)
                    return redirect(url_for("dashboard.dashboard_page"))
                else:
                    flash("Login failed.", category="alert")
                    return redirect(url_for("user.login_page"))
            else:
                flash("Invalid.")
                return redirect(url_for("user.login_page"))


@user_bp.route("/logout", methods=["GET"])
@login_required
def logout_page():
    logout_user()
    return redirect(url_for("main.index"))


@user_bp.route("/register", methods=["GET", "POST"])
def register_page():
    if current_user.is_active:
        flash("You have logined.", category="info")
        return redirect(url_for("dashboard.dashboard_page"))
    else:
        form = RegisterForm()
        if request.method == "GET":
            return render_template("register.html", form=form)
        if request.method == "POST":
            if form.validate_on_submit():
                username = form.username.data
                password = form.password.data
                email = form.email.data
                language = form.language.data
                if register(username, password, email, language):
                    flash("Register successfully.", category="success")
                    return redirect(url_for("user.login_page"))
                else:
                    flash("The name has been used.", category="alert")
                    return redirect(url_for("user.register_page"))
            else:
                for _, errors in form.errors.items():
                    for error in errors:
                        flash(error, category="alert")
                return redirect(url_for("user.register_page"))

@user_bp.route("/user_setting", methods=["GET", "POST"])
@login_required
def user_setting_page():
    user_data = render_user_data(current_user.id)
    form = UserSettingForm(email=user_data["email"], language=user_data["language"])
    if request.method == "GET":
        return render_template("user_setting.html", form=form)
    if request.method == "POST":
        if form.validate_on_submit():
            password = form.password.data
            email = form.email.data
            language = form.language.data
            if update_user(current_user.id, password, email, language):
                return redirect(url_for("dashboard.dashboard_page"))
        return redirect(url_for("user.user_setting_page"))
