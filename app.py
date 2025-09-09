from flask import Flask
from src.config.data_base import init_db, db
from src.routes import init_routes

def create_app():
    app = Flask(__name__)
    init_db(app)
    init_routes(app)
    return app

app = create_app()

with app.app_context():
    #db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)