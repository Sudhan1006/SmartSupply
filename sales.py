
class Sales:
    def __init__(self, db):
        self.db = db

    def record_sale(self, product_id, quantity):
        self.db.cursor.execute(
            "SELECT price, stock FROM products WHERE id=?",
            (product_id,)
        )
        product = self.db.cursor.fetchone()

        if product:
            price, stock = product
            if stock >= quantity:
                total = price * quantity

                self.db.cursor.execute(
                    "INSERT INTO sales (product_id, quantity, total) VALUES (?, ?, ?)",
                    (product_id, quantity, total)
                )

                self.db.cursor.execute(
                    "UPDATE products SET stock=? WHERE id=?",
                    (stock - quantity, product_id)
                )

                self.db.conn.commit()
                return True
        return False

    def get_sales(self):
        self.db.cursor.execute("SELECT * FROM sales")
        return self.db.cursor.fetchall()
