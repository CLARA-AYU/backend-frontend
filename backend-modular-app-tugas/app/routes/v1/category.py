from flask import Blueprint, request
from app.repositories.product_repo import ProductRepository
from app.utils.response_helper import success_response, fail_response

category_bp = Blueprint('categories', __name__, url_prefix='/api/v1/categories')
repo = ProductRepository()

@category_bp.route('', methods=['GET'])
def get_categories():
    products = repo.get_all()
    unique_categories = list(set(p["category"] for p in products if "category" in p))
    data = [{"id": index + 1, "name": cat} for index, cat in enumerate(unique_categories)]
    return success_response(data=data)

@category_bp.route('', methods=['POST'])
def create_category():
    data = request.get_json() if request.is_json else None
    if not data or not data.get("name"):
        return fail_response(errors={"name": "Nama kategori wajib diisi"}, code=400)
        
    return success_response(
        data={"id": 99, "name": data["name"]}, 
        message="Kategori berhasil dibuat", 
        code=201
    )