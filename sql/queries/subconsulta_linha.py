from sql.connection import get_connection

def subconsulta_linha():
    """
    Executa uma subconsulta de linha para obter o médico que realizou a última consulta.
    """
    print("Executando subconsulta de linha para obter o médico da última consulta...")
    
    # Consulta SQL para obter o médico da última consulta

    x = [
        """
        SELECT *
        FROM MEDICO
        WHERE (cpf, cod_crm) = (
            SELECT medico_cpf, cod_crm
            FROM MEDICO m
            INNER JOIN CONSULTA c on m.cpf = c.medico_cpf
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
            print(f'CPF: {r[0]}\nCódigo: {r[1]}')  # Imprime os detalhes do médico

    conn.close()