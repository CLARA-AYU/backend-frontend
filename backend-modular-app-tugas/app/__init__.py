from flask import Flask
from app.routes.product_routes import product_bp
from app.routes.v1.user_routes import user_bp_v1
from app.routes.v1.category import category_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(product_bp)
    app.register_blueprint(user_bp_v1)
    app.register_blueprint(category_bp)
    return app