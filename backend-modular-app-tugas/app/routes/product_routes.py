from flask import Blueprint, request
from app.repositories.product_repo import ProductRepository
from app.services.product_service import ProductService
from app.utils.response_helper import success_response, fail_response 

product_bp = Blueprint('products', __name__, url_prefix='/api/v1/products')
repo = ProductRepository()
service = ProductService(repo)

@product_bp.route('', methods=['GET'])
def list_products():
    return success_response(data=service.fetch_products())

@product_bp.route('/<int:product_id>', methods=['GET'])
def find_product(product_id):
    resp, code = service.get_product_details(product_id)
    if code != 200:
        return fail_response(errors=resp, code=code)
    return success_response(data=resp.get("data"))

@product_bp.route('', methods=['POST'])
def create_product():
    data = request.get_json() if request.is_json else None
    resp, code = service.add_new_product(data)
    if code != 201:
        return fail_response(errors=resp, code=code)
    return success_response(data=resp.get("data"), message="Produk berhasil ditambahkan", code=201)

@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json() if request.is_json else {}
    resp, code = service.update_product(product_id, data)
    if code != 200:
        return fail_response(errors=resp, code=code)
    return success_response(data=resp.get("data"), message="Produk berhasil diperbarui")

@product_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    resp, code = service.delete_product(product_id)
    if code != 200:
        return fail_response(errors=resp, code=code)
    return success_response(message="Produk berhasil dihapus")