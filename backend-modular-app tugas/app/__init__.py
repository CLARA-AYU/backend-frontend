from flask import Flask
from app.routes.product_routes import product_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(product_bp)
    return app