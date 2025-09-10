from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()

def init_db(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:root@localhost:3306/market_management"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)

    with app.app_context():
        #db.drop_all()
        db.create_all()
