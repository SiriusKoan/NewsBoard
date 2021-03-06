from os import getenv

class Config:
    DEBUG = True
    SECRET_KEY = getenv("APP_SECRET_KEY")
    ENV = "development"
    RECAPTCHA_ENABLED = True
    RECAPTCHA_PUBLIC_KEY = getenv("RECAPTCHA_PUBLIC_KEY")
    RECAPTCHA_PRIVATE_KEY = getenv("RECAPTCHA_PRIVATE_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///../../data.db"
    
class DevelopmentConfig(Config):
    pass

config_list = {
    'development': DevelopmentConfig,
}