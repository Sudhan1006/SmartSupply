
import pandas as pd

class Analytics:
    def __init__(self, db):
        self.db = db

    def sales_report(self):
        query = """
        SELECT p.name, SUM(s.quantity) as total_qty, SUM(s.total) as revenue
        FROM sales s
        JOIN products p ON s.product_id = p.id
        GROUP BY p.name
        """
        df = pd.read_sql(query, self.db.conn)
        return df
