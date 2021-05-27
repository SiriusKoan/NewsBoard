from . import main_bp
from ..db import db
from os import listdir
from flask_login import current_user
from flask import redirect, render_template, url_for


@main_bp.before_app_first_request
def db_check():
    if "data.db" not in listdir("../"):
        db.create_all()


@main_bp.route("/", methods=["GET", "POST"])
def index():
    if current_user.is_active:
        return redirect(url_for("dashboard.dashboard_page"))
    else:
        return render_template("index.html")
