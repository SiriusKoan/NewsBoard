from os import getenv

class Config:
    DEBUG = True
    SECRET_KEY = ""
    ENV = "development"
    RECAPTCHA_ENABLED = True
    RECAPTCHA_SITE_KEY = getenv("RECAPTCHA_SITE_KEY")
    RECAPTCHA_SECRET_KEY = getenv("RECAPTCHA_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///../../data.db"
    
class DevelopmentConfig(Config):
    pass

config_list = {
    'development': DevelopmentConfig,
}