from flask import Flask
from app.extensions.database import db
from app.extensions.migrate import migrate
from app.extensions.flask_login import lm


def create_app(config_class="app.config.DevelopmentConfig"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    lm.init_app(app)

    from app.Controllers.consumo_controller import consumo_bp
    from app.Controllers.user_controller import user_bp
    from app.views.auth_routes import auth_bp
    from app.views.post_routes import post_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(post_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(consumo_bp)

    from app.error_handlers import register_error_handlers
    register_error_handlers(app)

    return app