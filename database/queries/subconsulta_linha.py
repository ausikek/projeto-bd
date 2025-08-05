import sqlite3
from database.connection import get_connection

x = [
    """
    SELECT *
    FROM MEDICO
    WHERE cpf = (
        SELECT medico_cpf
        FROM CONSULTA
        WHERE data = (
            SELECT MAX(data)
            FROM CONSULTA
        )
    );
    """
]

conn = get_connection()
cur = conn.cursor()

for query in x:
    cur.execute(query)
    resultados = cur.fetchall()
    for r in resultados:
        print(r)

conn.close()