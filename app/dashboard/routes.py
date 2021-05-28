from . import dashboard_bp
from flask import render_template
from flask_login import login_required


# url prefix: /dashboard
@dashboard_bp.route("/")
@login_required
def dashboard_page():
    return render_template("dashboard.html")
