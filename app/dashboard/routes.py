from flask_login import login_required, current_user
from flask import request, render_template, abort
from . import dashboard_bp
from ..news_tools import (
    add_directory,
    delete_keyword,
    get_directories,
    delete_directory,
    add_keyword,
    render_directory,
)


# url prefix: /dashboard
@dashboard_bp.route("/", methods=["GET"])
@login_required
def dashboard_page():
    return render_template(
        "dashboard.html", directories=get_directories(current_user.id)
    )


@dashboard_bp.route("/backend", methods=["POST", "DELETE"])
@login_required
def dashboard_backend():
    if request.method == "POST":
        data = request.get_json(force=True)
        type = data.get("type", None)
        if type:
            if type == "keyword":
                directory_id = data.get("directory_id", None)
                keyword = data.get("keyword", None)
                if directory_id and keyword:
                    if add_keyword(directory_id, keyword):
                        return "OK"
            if type == "directory":
                value = data.get("value", None)
                if value:
                    if add_directory(current_user.id, value):
                        return "OK"
        abort(400)
    if request.method == "DELETE":
        data = request.get_json(force=True)
        type = data.get("type", None)
        if type:
            if type == "keyword":
                directory_id = data.get("directory_id", None)
                keyword = data.get("keyword", None)
                if directory_id and keyword:
                    if delete_keyword(directory_id, keyword):
                        return "OK"
            if type == "directory":
                directory_id = data.get("id", None)
                if directory_id:
                    if delete_directory(directory_id):
                        return "OK"
        abort(400)


@dashboard_bp.route("/directory/<string:directory_name>", methods=["GET"])
@login_required
def get_directory_page(directory_name):
    if directory := render_directory(current_user.id, directory_name):
        return render_template("directory_page.html", directory=directory)
    else:
        abort(404)
