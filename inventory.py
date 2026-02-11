
class Inventory:
    def __init__(self, db):
        self.db = db

    def add_product(self, name, price, stock):
        self.db.cursor.execute(
            "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
            (name, price, stock)
        )
        self.db.conn.commit()

    def get_products(self):
        self.db.cursor.execute("SELECT * FROM products")
        return self.db.cursor.fetchall()

    def update_stock(self, product_id, new_stock):
        self.db.cursor.execute(
            "UPDATE products SET stock=? WHERE id=?",
            (new_stock, product_id)
        )
        self.db.conn.commit()
