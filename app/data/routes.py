from flask import render_template
from . import data_bp

@data_bp.route("/data")
def data():
    return render_template("data/index.html")
