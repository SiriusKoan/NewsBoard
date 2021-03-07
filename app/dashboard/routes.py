from . import dashboard_bp
from flask_login import login_required

@dashboard_bp.route("/")
@login_required
def dashboard_page():
    return "dashboard"