from flask import Blueprint, request, jsonify
from app.repositories.product_repo import ProductRepository
from app.services.product_service import ProductService

product_bp = Blueprint('products', __name__, url_prefix='/api/v1/products')
repo = ProductRepository()
service = ProductService(repo)

@product_bp.route('', methods=['GET'])
def list_products():
    return jsonify({"status": "success", "data": service.fetch_products()}), 200

@product_bp.route('/<int:product_id>', methods=['GET'])
def find_product(product_id):
    resp, code = service.get_product_details(product_id)
    return jsonify(resp), code

@product_bp.route('', methods=['POST'])
def create_product():
    data = request.get_json() if request.is_json else None
    resp, code = service.add_new_product(data)
    return jsonify(resp), code

@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json() if request.is_json else {}
    resp, code = service.update_product(product_id, data)
    return jsonify(resp), code

@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    resp, code = service.delete_product(product_id)
    return jsonify(resp), code