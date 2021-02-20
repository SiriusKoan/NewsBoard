class Config:
    DEBUG = True
    SECRET_KEY = ""
    ENV = "development"
    RECAPTCHA_ENABLED = True
    RECAPTCHA_SITE_KEY = ""
    RECAPTCHA_SECRET_KEY = ""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"