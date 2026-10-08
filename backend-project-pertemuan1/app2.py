from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database simulasi untuk data produk
products = [
    {"id": 1, "name": "Laptop ThinkPad", "price": 12500000},
    {"id": 2, "name": "Mouse Wireless", "price": 250000}
]

# 1. HTTP GET: Mengambil Seluruh Koleksi Produk
@app.route('/api/v1/products', methods=['GET'])
def get_all_products():
    return jsonify({
        "status": "success",
        "total": len(products),
        "data": products
    }), 200

# 2. HTTP POST: Menambahkan Produk Baru
@app.route('/api/v1/products', methods=['POST'])
def create_product():
    # Memvalidasi Content-Type request harus JSON
    if not request.is_json:
        return jsonify({
            "status": "error",
            "message": "Payload harus berformat application/json"
        }), 400

    data = request.get_json()
    if "name" not in data or "price" not in data:
        return jsonify({
            "status": "error",
            "message": "Field 'name' dan 'price' wajib diisi"
        }), 400

    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"]
    }
    products.append(new_product)
    return jsonify({
        "status": "success",
        "message": "Produk berhasil ditambahkan",
        "data": new_product
    }), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)