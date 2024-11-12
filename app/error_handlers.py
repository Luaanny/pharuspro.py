from flask import render_template

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html")

    def internal_error(error):
        render_template("errors/500.html")