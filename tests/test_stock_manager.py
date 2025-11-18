import os
import pytest

pytestmark = pytest.mark.skipif(
    os.getenv("CI") == "true",
    reason="Skip DB tests in CI where no MySQL server is available."
)


# tests/test_stock_manager.py
import unittest
from src.database import init_db, get_connection
from src.produit import Produit
from src.stock_manager import StockManager

class StockManagerTest(unittest.TestCase):

    def setUp(self):
        init_db()
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produits")
        conn.commit()
        conn.close()

    def test_total_stock(self):
        sm = StockManager()
        sm.ajouter_produit(Produit("Stylo", 1000, 2))
        sm.ajouter_produit(Produit("Crayon", 500, 4))
        self.assertEqual(1000*2 + 500*4, sm.total_stock())

if __name__ == '__main__':
    unittest.main()
