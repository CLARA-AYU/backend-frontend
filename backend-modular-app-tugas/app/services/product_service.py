class ProductService:
    def __init__(self, repo):
        self.repo = repo
        
    def fetch_products(self):
        return self.repo.get_all()
        
    def get_product_details(self, product_id):
        product = self.repo.get_by_id(product_id)
        if not product:
            return {"error": "Produk tidak ditemukan"}, 404
        return {"status": "success", "data": product}, 200
        
    def add_new_product(self, data):
        if not data or "name" not in data or "price" not in data or "stock" not in data:
            return {"error": "Nama, harga, dan stok wajib diisi"}, 400
            
        if data["price"] <= 0:
            return {"error": "Harga harus lebih besar dari 0"}, 400
            
        category = data.get("category", "Makanan")
        created = self.repo.create(data["name"], category, data["price"], data["stock"])
        return {"status": "success", "data": created}, 201

    def update_product(self, product_id, data):
        if not self.repo.get_by_id(product_id):
            return {"error": "Produk tidak ditemukan"}, 404
        
        if "price" in data and data["price"] <= 0:
             return {"error": "Harga harus lebih besar dari 0"}, 400

        updated = self.repo.update(product_id, data)
        return {"status": "success", "data": updated}, 200

    def delete_product(self, product_id):
        if not self.repo.get_by_id(product_id):
            return {"error": "Produk tidak ditemukan"}, 404
            
        self.repo.delete(product_id)
        return {"status": "success", "message": "Produk berhasil dihapus"}, 200