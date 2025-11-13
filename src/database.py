# src/database.py
import mysql.connector



def get_connection():
    return mysql.connector.connect(
        host="localhost",     # ou 127.0.0.1
        user="root",          # ton utilisateur MySQL
        password="passer123",          # ton mot de passe MySQL (vide si aucun)
        database="stock_db"   # la base doit exister
    )

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produits (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(255) NOT NULL,
        prix INT NOT NULL,
        quantite INT NOT NULL
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()
