import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def init_db(app):
    os.environ.pop("DATABASE_URL", None)
    
    DATABASE_URL = os.getenv("dburl")

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    os.environ["DATABASE_URL"] = DATABASE_URL

    db.init_app(app)


