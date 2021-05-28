from flask import render_template
from flask_login import login_required, current_user
from flask import flash, request, render_template
from . import dashboard_bp
from ..forms import AddNewDirectoryForm
from ..news_tools import create_directory, get_directories


# url prefix: /dashboard
@dashboard_bp.route("/", methods=["GET", "POST"])
@login_required
def dashboard_page():
    form = AddNewDirectoryForm()
    if request.method == "GET":
        return render_template("dashboard.html", form=form, directories=get_directories(current_user.id))
    if request.method == "POST":
        if form.validate_on_submit():
            directory_name = form.directory_name.data
            if create_directory(current_user.id, directory_name):
                flash("Success.", category="success")
            else:
                flash("Error.", category="alert")
        else:
            for _, errors in form.errors.items():
                for error in errors:
                    flash(error, category="alert")
        return render_template("dashboard.html", form=form)


@dashboard_bp.route("dashboard_backend", methods=["POST"])
def dashboard_backend():
    pass