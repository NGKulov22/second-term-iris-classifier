from flask import render_template
from flask_login import login_required, current_user
from . import main_bp

@main_bp.route("/")
def index():
    return render_template("main/index.html")

@main_bp.route("/index")
@login_required
def dashboard():
    return render_template("data/index.html", user=current_user)