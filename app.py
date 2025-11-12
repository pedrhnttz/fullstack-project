from flask import Flask
from flask_cors import CORS
from src.config.data_base import init_db, db
from src.routes import init_routes
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    app.config["JWT_SECRET_KEY"] = "plt"
    
    jwt = JWTManager(app)
    init_db(app)
    init_routes(app)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)