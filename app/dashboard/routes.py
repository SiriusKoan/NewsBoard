from flask_login import login_required, current_user
from flask import flash, request, render_template, abort
from . import dashboard_bp
from ..forms import AddNewDirectoryForm
from ..news_tools import (
    create_directory,
    delete_keyword,
    get_directories,
    delete_directory,
    add_keyword,
    render_directory,
)


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


@dashboard_bp.route("/backend", methods=["POST", "DELETE"])
@login_required
def dashboard_backend():
    if request.method == "POST":
        data = request.get_json(force=True)
        directory_id = data.get("id", None)
        keyword = data.get("keyword", None)
        if directory_id and keyword:
            if add_keyword(directory_id, keyword):
                return "OK"
        abort(400)
    if request.method == "DELETE":
        data = request.get_json(force=True)
        type = data.get("type", None)
        if type:
            if type == "directory":
                directory_id = data.get("id", None)
                if directory_id:
                    if delete_directory(directory_id):
                        return "OK"
                abort(400)
            if type == "keyword":
                directory_id = data.get("directory_id", None)
                keyword = data.get("keyword", None)
                if directory_id and keyword:
                    if delete_keyword(directory_id, keyword):
                        return "OK"
                abort(400)
        else:
            abort(400)


@dashboard_bp.route("/directory/<string:directory_name>", methods=["GET"])
@login_required
def get_directory_page(directory_name):
    if directory := render_directory(current_user.id, directory_name):
        return render_template("directory_page.html", directory=directory)
    else:
        abort(404)
