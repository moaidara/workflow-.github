# tests/test_produit.py
import unittest
import os
import pytest
from src.database import init_db, get_connection
from src.produit import Produit

pytestmark = pytest.mark.skipif(
    os.getenv("CI") == "true",
    reason="Skip DB tests in CI where no MySQL server is available."
)

class ProduitTest(unittest.TestCase):

    def setUp(self):
        init_db()
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produits")
        conn.commit()
        conn.close()

    def test_creation_produit(self):
        p = Produit("Stylo", 1000, 5)
        p.save()
        self.assertIsNotNone(p.id)
        self.assertEqual("Stylo", p.nom)
        self.assertEqual(5, p.quantite)

    def test_ajout_stock(self):
        p = Produit("Crayon", 500, 10)
        p.quantite += 5
        self.assertEqual(15, p.quantite)

if __name__ == '__main__':
    unittest.main()
