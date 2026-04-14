from flask import render_template
from flask_login import login_required, current_user
from . import results_bp
from app.models import Prediction

@results_bp.route("/results")
@login_required
def results():
    predictions = Prediction.query.filter_by(user_id=current_user.id).order_by(Prediction.id.asc()).all()
    last_prediction = Prediction.query.filter_by(user_id=current_user.id).order_by(Prediction.id.desc()).first()
    return render_template("results/index.html", predictions=predictions, last_prediction=last_prediction)