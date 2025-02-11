from flask import render_template

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html")

    @app.errorhandler(401)
    def unauthorized(error):
        render_template("errors/401.html")

    @app.errorhandler(505)
    def internal_error(error):
        render_template("errors/500.html")