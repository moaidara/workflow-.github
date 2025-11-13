# src/produit.py
from src.database import get_connection

class Produit:
    def __init__(self, nom, prix, quantite, id=None):
        self.id = id
        self.nom = nom
        self.prix = prix
        self.quantite = quantite

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        if self.id is None:
            cursor.execute(
                "INSERT INTO produits (nom, prix, quantite) VALUES (%s, %s, %s)",
                (self.nom, self.prix, self.quantite)
            )
            self.id = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE produits SET nom=%s, prix=%s, quantite=%s WHERE id=%s",
                (self.nom, self.prix, self.quantite, self.id)
            )

        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def find(id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produits WHERE id=%s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Produit(row["nom"], row["prix"], row["quantite"], row["id"]) if row else None

    @staticmethod
    def all():
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produits")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Produit(r["nom"], r["prix"], r["quantite"], r["id"]) for r in rows]
