import os
import json
import numpy as np
import pandas as pd
from .logistic_regression import LogisticRegression
from flask import current_app

class TrainModel:
    def __init__(self):
        self.model = LogisticRegression(lr=0.1, epochs=1000)
        self.model_path = "model.json"

    # ---------------- TRAIN ----------------
    def train(self):
        df = pd.read_csv("data/Iris.csv")
        df = df.drop(columns=["Id"])

        X = df[[
            "SepalLengthCm",
            "SepalWidthCm",
            "PetalLengthCm",
            "PetalWidthCm"
        ]].values

        y = (df["Species"] == "Iris-setosa").astype(int).values

        self.model.fit(X, y)
        self.save()

    # ---------------- SAVE ----------------
    def save(self):
        data = {
            "weights": self.model.weights.tolist(),
            "bias": float(self.model.bias)
        }

        with open(self.model_path, "w") as f:
            json.dump(data, f)

    # ---------------- LOAD ----------------
    def load(self):
        if not os.path.exists(self.model_path):
            return False

        with open(self.model_path, "r") as f:
            data = json.load(f)

        self.model.weights = np.array(data["weights"])
        self.model.bias = data["bias"]
        return True

    # ---------------- PREDICT ----------------
    def predict(self, X):
        return self.model.predict(X)

    def predict_proba(self, X):
        return self.model.predict_proba(X)