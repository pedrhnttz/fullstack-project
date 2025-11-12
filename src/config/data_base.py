import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()

def init_db(app):
    DATABASE_URL = os.getenv("DATABASE_URL")

    if DATABASE_URL and "psycopg2" in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("psycopg2", "psycopg")

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    if os.getenv("FLASK_ENV") == "development":
        with app.app_context():
            db.create_all()

