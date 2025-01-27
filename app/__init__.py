from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize SQLAlchemy
db = SQLAlchemy()

# Initialize Flask-Migrate
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Initialize db and migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Register routes
    from .routes import bp
    app.register_blueprint(bp)

    return app
