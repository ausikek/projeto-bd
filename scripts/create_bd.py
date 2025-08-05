#criar o bd

from database.connection import get_connection
from database.schema import schema_statements

def create_tables():
    conn = get_connection()
    cur = conn.cursor()
    for ddl in schema_statements:
        cur.execute(ddl)
    conn.commit()
    conn.close()
    print("Tabelas criadas com sucesso.")

if __name__ == "__main__":
    create_tables()