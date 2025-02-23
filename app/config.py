import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', "lua_linda")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "sqlite:///pharus.db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    login_view = 'auth_bp.login'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    DEBUG = False