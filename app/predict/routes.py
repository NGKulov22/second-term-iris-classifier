from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models import Prediction
from app import db
from . import predict_bp
from flask import current_app
from flask import current_app, render_template, request
from flask_login import login_required
from . import predict_bp
import numpy as np


@predict_bp.route("/predict", methods=["GET", "POST"])
@login_required
def predict():

    if request.method == "POST":

        # 1. input
        X = np.array([[
            float(request.form["sepal_length"]),
            float(request.form["sepal_width"]),
            float(request.form["petal_length"]),
            float(request.form["petal_width"])
        ]])

        # 2. model
        model = current_app.train_model

        # 3. prediction
        prob = model.predict(X)[0]
        pred = 1 if prob >= 0.5 else 0
        prob = float(model.predict_proba(X)[0])

        prob_setosa = float(model.predict_proba(X)[0])
        if prob_setosa >= 0.5:
            label = "Iris-setosa"
            confidence = prob_setosa
        else:
            label = "Not setosa"
            confidence = 1 - prob_setosa

        # 4. SAVE TO DB
        new_prediction = Prediction(
            sepal_length=X[0][0],
            sepal_width=X[0][1],
            petal_length=X[0][2],
            petal_width=X[0][3],
            prediction=label,
            probability=prob,
            user_id=current_user.id
        )

        db.session.add(new_prediction)
        db.session.commit()

        return redirect(url_for("predict.predict"))

    # GET → show page
    predictions = Prediction.query.filter_by(user_id=current_user.id).all()

    return render_template(
        "predict/index.html",
        predictions=predictions
    )
      

