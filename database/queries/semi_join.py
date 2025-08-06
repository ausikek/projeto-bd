from database.connection import get_connection

def semi_join_query():
    """
    Executa uma consulta SEMI JOIN que retorna os nomes dos presos que possuem advogados.
    """
    print("Executando consulta SEMI JOIN para obter nomes de presos com advogados...")

    # A consulta SQL que utiliza SEMI JOIN para filtrar presos com advogados
    y = [
        """
        SELECT pr.nome AS nome_preso
        FROM PRESO pr
        WHERE EXISTS (
            SELECT po.preso_cpf
            FROM POSSUI po
            WHERE po.preso_cpf = pr.cpf
        )
        ORDER BY pr.nome;
        """
    ]

    conn = get_connection()
    cur = conn.cursor()

    for query in y:
        cur.execute(query)
        resultados = cur.fetchall()
        for r in resultados:
            print(f"Preso: {r[0]}")

    conn.close()