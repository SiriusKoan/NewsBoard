from os import getenv


class Config:
    SECRET_KEY = getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Testing(Config):
    ENV = "TESTING"
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"


class Development(Config):
    ENV = "DEVELOPMENT"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"


class Production(Config):
    ENV = "PRODUCTION"
    SQLALCHEMY_DATABASE_URI = getenv("DATABASE_URI")


config_list = {
    "testing": Testing,
    "development": Development,
    "production": Production,
}
