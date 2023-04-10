import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.config['POSTERS_FOLDER'] = os.path.abspath('./posters')

db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here
migrate = Migrate(app, db)

from app import views
