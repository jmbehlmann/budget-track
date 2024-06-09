from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../instance/config.py')

    from . import db
    db.init_app(app)

    from . import routes
    app.register_blueprint(routes.bp)

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db.get_db()}

    return app
