from database.connection import get_connection

def union_query():
    """
    Executa uma consulta UNION que combina os nomes dos médicos e advogados.
    """
    print("Executando consulta UNION para combinar nomes de médicos e advogados...")

    # A consulta SQL que utiliza UNION para combinar os nomes de médicos e advogados
    y = [
        """
        SELECT f.nome AS nome_profissional, 'Médico' AS tipo
        FROM FUNCIONARIO f
        JOIN MEDICO m ON f.cpf = m.cpf
        UNION
        SELECT a.nome AS nome_profissional, 'Advogado' AS tipo
        FROM ADVOGADO a
        ORDER BY nome_profissional;
        """
    ]

    conn = get_connection()
    cur = conn.cursor()

    for query in y:
        cur.execute(query)
        resultados = cur.fetchall()
        for r in resultados:
            print(f"Nome: {r[0]}, Profissão: {r[1]}")

    conn.close()