from config import DB_FILE
from document.connection import get_mongo_client
from sql.connection import get_connection
from os import path, access, R_OK

def healthcheck() -> bool:
    """Check the health of the MongoDB connection."""
    try:
        client = get_mongo_client()
        client.admin.command('ping')
        
        print(">>> A conexão com o MongoDB está saudável.")
    except Exception as e:
        print(f">>> Erro de conexão com o MongoDB: {e}")
        return False

    """Check if prisional.db exists and is accessible."""
    try:
        if path.isfile(DB_FILE) and access(DB_FILE, R_OK):
            print(">>> Arquivo prisional.db encontrado e acessível.")
        else:
            print(">>> Arquivo prisional.db não encontrado ou não acessível.")
    except Exception as e:
        print(">>> Arquivo prisional.db não encontrado. Tentando criar novo arquivo...")
        
        try:
            with open(DB_FILE, 'w') as f:
                f.write("")
            print(">>> Arquivo prisional.db criado com sucesso.")
        except Exception as e:
            print(f">>> Erro ao criar o arquivo prisional.db: {e}")
            return False

    """Check the health of the SQL connection."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        print(">>> A conexão com o SQLite está saudável.")
    except Exception as e: 
        print(f">>> Erro de conexão com o SQLite: {e}")
        return False

    return True