#funcao de conexão
import sqlite3

DB_FILE = "prisional.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn