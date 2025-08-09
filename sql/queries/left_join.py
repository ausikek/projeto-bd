from sql.connection import get_connection

def left_join_query():
    """
    Executa uma consulta LEFT JOIN que retorna os nomes dos presídios e os números das celas, incluindo presídios sem celas atribuídas.
    """
    print("Executando consulta LEFT JOIN para obter os nomes dos presídios e suas celas...")

    # A consulta SQL que realiza o LEFT JOIN entre PRESIDIO e CELA para incluir presídios sem celas atribuídas
    y = [
        """
        SELECT p.cidade AS nome_presidio, c.num AS numero_cela
        FROM PRESIDIO p
        LEFT JOIN CELA c ON p.cod = c.presidio_cod
        ORDER BY p.cidade;
        """
    ]

    conn = get_connection()
    cur = conn.cursor()

    for query in y:
        cur.execute(query)
        resultados = cur.fetchall()
        for r in resultados:
            nome_presidio = r[0] if r[0] else "Desconhecido"
            numero_cela = r[1] if r[1] else "Sem cela"
            print(f"Presídio: {nome_presidio}, Cela: {numero_cela}")

    conn.close()