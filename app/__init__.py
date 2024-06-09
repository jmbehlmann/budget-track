from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../instance/config.py')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/budget.db'

    db.init_app(app)

    from . import routes, models
    app.register_blueprint(routes.bp)

    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        print("Database initialized successfully.")

    return app

