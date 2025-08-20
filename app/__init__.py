from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
# 'main.login' will be the name of our login route
login_manager.login_view = 'main.login'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '8w5h4J2k9L7p6T1s3G0q8R5f4P9x7M1n0B3v2C6z4Y8d0E9u7'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    login_manager.init_app(app)

    # User loader function for Flask-Login
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .routes import main_blueprint
    app.register_blueprint(main_blueprint)

    from . import models
    with app.app_context():
        db.create_all()

    return app
