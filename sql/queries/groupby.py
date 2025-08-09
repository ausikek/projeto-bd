from sql.connection import get_connection

def groupby_query():
    """
    Executa consultas GROUP BY que retornam a quantidade de funcionários por presídio,
    incluindo uma subconsulta e outra usando HAVING para filtrar presídios com mais de 2 funcionários.
    """
    print("Executando consulta GROUP BY para obter a quantidade de funcionários por presídio...")

    queries = [
        # GROUP BY: Quantidade de funcionários por presídio
        """
        SELECT p.cod, COUNT(f.cpf) AS total_funcionarios
        FROM PRESIDIO p
        LEFT JOIN FUNCIONARIO f ON f.presidio_cod = p.cod
        GROUP BY p.cod
        ORDER BY total_funcionarios DESC;
        """,
        # HAVING: Apenas presídios com mais de 2 funcionários
        """
        SELECT p.cod, COUNT(f.cpf) AS total_funcionarios
        FROM PRESIDIO p
        LEFT JOIN FUNCIONARIO f ON f.presidio_cod = p.cod
        GROUP BY p.cod
        HAVING COUNT(f.cpf) > 2
        ORDER BY total_funcionarios DESC;
        """
    ]

    conn = get_connection()
    cur = conn.cursor()

    for idx, query in enumerate(queries, 1):
        if idx == 1:
            print("\nConsulta 1: Quantidade de funcionários por presídio (sem HAVING)")
        else:
            print("\nConsulta 2: Presídios com mais de 2 funcionários (com HAVING)")
        cur.execute(query)
        resultados = cur.fetchall()
        for r in resultados:
            print(f"Código do presídio: {r[0]}, Total de funcionários: {r[1]}")

    conn.close()