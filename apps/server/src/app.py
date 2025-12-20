from flask import Flask
from flask_cors import CORS
from src.routes.users import user_routes


def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route("/api/", methods=["GET"])
    def health_check():
        return "OK", 200

    app.register_blueprint(user_routes, url_prefix="/api/users")

    return app
