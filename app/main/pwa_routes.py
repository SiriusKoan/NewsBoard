from flask import current_app
from . import main_bp


@main_bp.route("/sw.js")
def return_sw():
    return current_app.send_static_file("pwa/sw.js")


@main_bp.route("/manifest.json")
def return_manifest():
    return current_app.send_static_file("pwa/manifest.json")


@main_bp.route("/app/static/app.js")
def return_app_js():
    return current_app.send_static_file("pwa/app.js")
