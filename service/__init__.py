"""
Customer Accounts Microservice
"""
import os

from flask import Flask, jsonify
from flask_cors import CORS
from flask_talisman import Talisman

from service.models import db
from service.routes import api


def create_app(config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)

    # Talisman security headers. The Content-Security-Policy is disabled so the
    # service can be exercised from a browser / curl during the labs.
    Talisman(app, content_security_policy=None, force_https=False)

    # CORS policies: allow the Accounts UI (and other clients) to call the API.
    CORS(
        app,
        resources={r"/*": {"origins": "*"}},
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        expose_headers=["X-Total-Count"],
    )

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "secret-for-dev")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URI", "sqlite:///accounts.db"
    )

    if config:
        app.config.update(config)

    db.init_app(app)
    app.register_blueprint(api)

    @app.route("/")
    def index():
        return (
            jsonify(
                service="Accounts Microservice",
                status="OK",
                version="1.0",
                endpoints={
                    "accounts": "/accounts",
                    "health": "/health",
                },
            ),
            200,
        )

    @app.route("/health")
    def health():
        return jsonify(status="OK"), 200

    return app


app = create_app()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8080)
