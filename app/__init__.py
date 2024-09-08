from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize Flask app
app = Flask(__name__)

# Configurations
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookify.db'

# Initialize the database
db = SQLAlchemy(app)

# Initialize the login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import the routes after initializing app, db, and login_manager
from app import routes

# Define the user_loader function after importing routes
@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))