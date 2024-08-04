from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .utils import format_date

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../instance/config.py')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/budget.db'

    app.jinja_env.filters['format_date'] = format_date

    db.init_app(app)

    from .home import home_bp
    from .transactions import transactions_bp
    from .budgets import budgets_bp
    from .categories import categories_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(transactions_bp, url_prefix='/transactions')
    app.register_blueprint(budgets_bp, url_prefix='/budgets')
    app.register_blueprint(categories_bp, url_prefix='/categories')


    # from . import routes, models
    # app.register_blueprint(routes.bp)

    @app.cli.command("init-db")
    def init_db():
        db.create_all()
        print("Database initialized successfully.")

    return app

