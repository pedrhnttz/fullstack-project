import os
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port")
DBNAME = os.getenv("dbname")

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"

db = SQLAlchemy()

def init_db(app):
    global DATABASE_URL

    if DATABASE_URL and "psycopg2" in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("psycopg2", "psycopg")

    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    os.environ["DATABASE_URL"] = DATABASE_URL

