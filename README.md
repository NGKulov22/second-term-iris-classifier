# 🌸 Iris Flower Classifier (Flask + Logistic Regression)

## 📌 Project Goal
The goal of this project is to develop a Flask web application that demonstrates the practical use of a machine learning algorithm implemented from scratch.  

The application allows users to interact with a Logistic Regression model trained on the Iris dataset and make predictions through a web interface.

---

## 🤖 Chosen Algorithm
**Logistic Regression (implemented from scratch)**

The model is built manually using:
- Python
- NumPy
- Pandas  

No external machine learning libraries (such as scikit-learn) are used.

---

## 📊 Dataset Description
The project uses the **Iris dataset**, which contains 150 samples of iris flowers divided into three classes:

- Iris-setosa  
- Iris-versicolor  
- Iris-virginica  

Each sample includes the following features:
- Sepal Length  
- Sepal Width  
- Petal Length  
- Petal Width  

In this project, the task is simplified to **binary classification**:
- `1 → Iris-setosa`
- `0 → Not setosa`

---

## ⚙️ Features

- ✅ User Registration and Login (Flask-Login)
- ✅ Password hashing and authentication
- ✅ Protected routes
- ✅ Input forms using Flask-WTF
- ✅ Logistic Regression model (from scratch)
- ✅ Model training on Iris dataset
- ✅ Prediction based on user input
- ✅ Probability output
- ✅ Saving predictions to database
- ✅ Prediction history per user
- ✅ Clean modular structure using Blueprints

---

## 🏗️ Technologies Used

- Flask  
- Flask-Login  
- Flask-WTF  
- Flask-SQLAlchemy  
- SQLite  
- Pandas  
- NumPy  


## 🚀 Installation

1. Clone the repository
2. Create virtual environment
3. Install dependencies:
    pip install -r requirements.txt
4. Run the Application
