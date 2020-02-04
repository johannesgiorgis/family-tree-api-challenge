"""
Configuration Information for Flask App
"""

from pathlib import Path

import connexion
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

base_dir = Path(__file__).parent.absolute()

# Create the connexion application instance
swagger_dir = str(base_dir) + "/swagger/"
connex_app = connexion.App(__name__, specification_dir=swagger_dir)

# Get the underlying Flask app instance
app = connex_app.app

# Build the SQLite URL for SQLAlchemy
sqlite_path = str(base_dir.joinpath("db/family.sqlite"))
sqlite_url = "sqlite:////" + sqlite_path

# Configure the SQLAlchemy db instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)
