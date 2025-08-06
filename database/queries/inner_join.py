from database.connection import get_connection

def inner_join_query():
    """
    Executa uma consulta INNER JOIN que retorna os nomes dos presos e os nomes dos advogados responsáveis por eles.
    """
    print("Executando consulta INNER JOIN para obter os nomes dos presos e seus advogados...")

    # A consulta SQL que realiza o INNER JOIN entre PRESO e ADVOGADO através da tabela POSSUI
    y = [
        """
        SELECT pr.nome AS nome_preso, adv.nome AS nome_advogado
        FROM PRESO pr
        INNER JOIN POSSUI po ON pr.cpf = po.preso_cpf
        INNER JOIN ADVOGADO adv ON po.advogado_cpf = adv.cpf
        ORDER BY pr.nome;
        """
    ]

    conn = get_connection()
    cur = conn.cursor()

    for query in y:
        cur.execute(query)
        resultados = cur.fetchall()
        for r in resultados:
            print(f"Preso: {r[0]}, Advogado: {r[1]}")

    conn.close()