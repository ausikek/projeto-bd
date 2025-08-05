import sqlite3
from database.connection import get_connection

y = [
    #o codigo do presidio que tenha a maior lotacao_atual
    """
    SELECT cod
    FROM PRESIDIO p
    WHERE lotacao_atual = (
        SELECT MAX(lotacao_atual)
        FROM PRESIDIO
        );
    """
]

conn = get_connection()
cur = conn.cursor()

for query in y:
    cur.execute(query)
    resultados = cur.fetchall()
    for r in resultados:
        print(r)

conn.close()