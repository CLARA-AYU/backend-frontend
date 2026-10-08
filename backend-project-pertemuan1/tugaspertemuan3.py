from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock Dataset Kategori & Barang UMKM
categories_dataset = [
    {"id": 1, "name": "Makanan"},
    {"id": 2, "name": "Minuman"}
]

items_dataset = [
    {"id": 1, "name": "Kripik Singkong Balado", "category": "Makanan", "price": 15000, "stock": 50},
    {"id": 2, "name": "Kopi Arabika Gayo 250g", "category": "Minuman", "price": 75000, "stock": 30},
    {"id": 3, "name": "Tas Tenun Tradisional", "category": "Kerajinan", "price": 180000, "stock": 12},
    {"id": 4, "name": "Sambal Roa Manado", "category": "Makanan", "price": 35000, "stock": 40},
    {"id": 5, "name": "Madu Hutan Asli 500ml", "category": "Minuman", "price": 120000, "stock": 20},
    {"id": 6, "name": "Gantungan Kunci Kayu", "category": "Kerajinan", "price": 10000, "stock": 100}
]


# ==========================================
# ENDPOINT: KATEGORI
# ==========================================

@app.route('/api/v1/categories', methods=['GET'])
def get_categories():
    """Mengambil seluruh data kategori"""
    return jsonify({
        "status": "success",
        "total": len(categories_dataset),
        "data": categories_dataset
    }), 200


# ==========================================
# ENDPOINT: BARANG (ITEMS)
# ==========================================

@app.route('/api/v1/items', methods=['GET'])
def get_items():
    """
    Mengambil seluruh data barang dengan dukungan Query Parameter:
    - ?category=...
    - ?min_price=...
    """
    category_query = request.args.get('category')
    min_price_query = request.args.get('min_price')

    filtered_items = items_dataset

    # Filter berdasarkan kategori jika ada
    if category_query:
        filtered_items = [
            item for item in filtered_items 
            if item['category'].lower() == category_query.lower()
        ]

    # Filter berdasarkan harga minimum jika ada
    if min_price_query:
        try:
            min_price = float(min_price_query)
            filtered_items = [
                item for item in filtered_items 
                if item['price'] >= min_price
            ]
        except ValueError:
            return jsonify({
                "status": "fail",
                "message": "Parameter min_price harus berupa angka valid"
            }), 400

    return jsonify({
        "status": "success",
        "total": len(filtered_items),
        "data": filtered_items
    }), 200


@app.route('/api/v1/items/<int:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    """Mengambil detail barang berdasarkan ID (Path Parameter integer)"""
    item = next((i for i in items_dataset if i['id'] == item_id), None)
    
    if not item:
        return jsonify({
            "status": "fail",
            "message": "Barang tidak ditemukan"
        }), 404

    return jsonify({
        "status": "success",
        "data": item
    }), 200


@app.route('/api/v1/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """Memperbarui data barang berdasarkan ID"""
    item = next((i for i in items_dataset if i['id'] == item_id), None)
    
    if not item:
        return jsonify({
            "status": "fail",
            "message": "Barang tidak ditemukan"
        }), 404

    request_data = request.get_json()
    if not request_data:
        return jsonify({
            "status": "fail",
            "message": "Payload JSON tidak boleh kosong"
        }), 400

    # Update atribut jika disediakan dalam request body
    item['name'] = request_data.get('name', item['name'])
    item['category'] = request_data.get('category', item['category'])
    item['price'] = request_data.get('price', item['price'])
    item['stock'] = request_data.get('stock', item['stock'])

    return jsonify({
        "status": "success",
        "message": "Data barang berhasil diperbarui",
        "data": item
    }), 200


@app.route('/api/v1/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Menghapus data barang berdasarkan ID"""
    global items_dataset
    item = next((i for i in items_dataset if i['id'] == item_id), None)
    
    if not item:
        return jsonify({
            "status": "fail",
            "message": "Barang tidak ditemukan"
        }), 404

    items_dataset = [i for i in items_dataset if i['id'] != item_id]

    return jsonify({
        "status": "success",
        "message": "Data barang berhasil dihapus"
    }), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)