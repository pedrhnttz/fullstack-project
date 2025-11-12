from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def init_db(app):

    load_dotenv()

    DATABASE_URL = os.getenv("DATABASE_URL")

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    engine = create_engine(DATABASE_URL)
    if not database_exists(engine.url):
        create_database(engine.url)

    with app.app_context():
        db.drop_all()
        db.create_all()
