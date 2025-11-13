# src/stock_manager.py
from src.produit import Produit

class StockManager:
    def ajouter_produit(self, produit):
        produit.save()

    def total_stock(self):
        produits = Produit.all()
        return sum(p.prix * p.quantite for p in produits)
