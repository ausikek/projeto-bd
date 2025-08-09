#criar o bd

from sql.connection import get_connection
from sql.schema import schema_statements

def create_tables():
    conn = get_connection()
    cur = conn.cursor()
    for ddl in schema_statements:
        cur.execute(ddl)
    conn.commit()
    conn.close()
    print(">> Tabelas criadas com sucesso.")