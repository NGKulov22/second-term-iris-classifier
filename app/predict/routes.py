from flask import render_template
from . import predict_bp

@predict_bp.route("/predict")
def predict():
    return render_template("predict/index.html")
