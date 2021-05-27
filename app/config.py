from os import getenv


class Config:
    SECRET_KEY = getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///../../data.db"


class Testing(Config):
    ENV = "TESTING"
    TESTING = True


class Development(Config):
    ENV = "DEVELOPMENT"
    DEBUG = True


class Production(Config):
    ENV = "PRODUCTION"


config_list = {
    "testing": Testing,
    "development": Development,
    "production": Production,
}
