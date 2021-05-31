from flask_login import login_required, current_user
from flask import flash, request, render_template, abort
from . import dashboard_bp
from ..forms import AddNewDirectoryForm
from ..news_tools import create_directory, get_directories, add_keyword


# url prefix: /dashboard
@dashboard_bp.route("/", methods=["GET", "POST"])
@login_required
def dashboard_page():
    form = AddNewDirectoryForm()
    if request.method == "GET":
        return render_template(
            "dashboard.html", form=form, directories=get_directories(current_user.id)
        )
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
        return render_template(
            "dashboard.html", form=form, directories=get_directories(current_user.id)
        )


@dashboard_bp.route("/backend", methods=["POST"])
@login_required
def dashboard_backend():
    if request.method == "POST":
        data = request.get_json(force=True)
        directory_id = data["id"]
        keyword = data["keyword"]
        if add_keyword(directory_id, keyword):
            return "OK"
        else:
            abort(400)
