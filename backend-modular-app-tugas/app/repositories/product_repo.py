class ProductRepository:
    def __init__(self):
        self.products = [
            { "id": 1, "name": "Tahu kocek original", "category": "Makanan", "price": 10000, "stock": 24 },
            { "id": 2, "name": "Tahu kocek sosis", "category": "Makanan", "price": 10000, "stock": 27 },
            { "id": 3, "name": "Tahu kocek tempura", "category": "Makanan", "price": 10000, "stock": 21 },
            { "id": 4, "name": "Tahu kocek sosis mix tempura", "category": "Makanan", "price": 15000, "stock": 23 },
            { "id": 5, "name": "Tahu kocek basreng", "category": "Makanan", "price": 10000, "stock": 22 },
            { "id": 6, "name": "Tahu kocek tempura mix basreng", "category": "Makanan", "price": 15000, "stock": 26 },
            { "id": 7, "name": "Tahu kocek basreng mix sosis", "category": "Makanan", "price": 15000, "stock": 25 },
            { "id": 8, "name": "Tahu kocek cireng", "category": "Makanan", "price": 15000, "stock": 29 },
            { "id": 9, "name": "Tahu kocek keju", "category": "Makanan", "price": 15000, "stock": 23 },
            { "id": 10, "name": "Tahu kocek keju mix sosis", "category": "Makanan", "price": 15000, "stock": 21 }
]

    def get_all(self):
        return self.products

    def get_by_id(self, product_id):
        return next((p for p in self.products if p["id"] == product_id), None)

    def create(self, name, category, price, stock):
        product = {
            "id": len(self.products) + 1, 
            "name": name, 
            "category": category,
            "price": price,
            "stock": stock
        }
        self.products.append(product)
        return product

    def update(self, product_id, data):
        product = self.get_by_id(product_id)
        if product:
            for key, value in data.items():
                if key in product:
                    product[key] = value
            return product
        return None

    def delete(self, product_id):
        product = self.get_by_id(product_id)
        if product:
            self.products.remove(product)
            return True
        return False