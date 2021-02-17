class Config:
    DEBUG = True
    SECRET_KEY = "asdasdasdasasdasdasdasd"
    ENV = "development"
    RECAPTCHA_ENABLED = True
    RECAPTCHA_SITE_KEY = "6Lc7UMUUAAAAAEVWlNxm5SNF7kaiixUZAVBoyNVc"
    RECAPTCHA_SECRET_KEY = "6Lc7UMUUAAAAALl0APCC9dCjzKKOz0Cgys1K91q1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///data.db"