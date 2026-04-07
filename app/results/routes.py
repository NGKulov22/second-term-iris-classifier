from flask import render_template
from . import results_bp

@results_bp.route("/results")
def results():
    return render_template("results/index.html")
