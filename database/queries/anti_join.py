from database.connection import get_connection

def anti_join_query():
    """
    Executa uma consulta ANTI JOIN que retorna os nomes dos médicos que não possuem consultas agendadas.
    """
    print("Executando consulta ANTI JOIN para obter nomes de médicos sem consultas agendadas...")

    # A consulta SQL que utiliza ANTI JOIN para filtrar médicos sem consultas realizadas
    y = [
        """
        SELECT f.nome AS nome_medico
        FROM FUNCIONARIO f
        JOIN MEDICO m ON f.cpf = m.cpf
        WHERE NOT EXISTS (
            SELECT c.medico_cpf
            FROM CONSULTA c
            WHERE c.medico_cpf = m.cpf
        )
        ORDER BY f.nome;
        """
    ]

    conn = get_connection()
    cur = conn.cursor()

    for query in y:
        cur.execute(query)
        resultados = cur.fetchall()
        for r in resultados:
            print(f"Médico: {r[0]}")

    conn.close()