class Config:
    SECRET_KEY = "dev_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///iris.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False