from sql.connection import get_connection

def table_subquery():
    """
    Executa uma subconsulta em tabela que retorna as consultas médicas realizadas, mostrando o médico responsável e os detalhes do prontuário.
    """
    print("Executando subconsulta em tabela para obter consultas médicas...")

    # A consulta SQL que realiza um JOIN entre CONSULTA e FUNCIONARIO para mostrar médicos e suas consultas
    y = [
        """
        SELECT s.data_consulta, s.nome_medico, s.detalhes_prontuario
        FROM (
            SELECT c.data AS data_consulta, f.nome AS nome_medico, c.prontuario AS detalhes_prontuario
            FROM CONSULTA c
            JOIN MEDICO m ON c.medico_cpf = m.cpf
            JOIN FUNCIONARIO f ON m.cpf = f.cpf
        ) AS s
        ORDER BY s.data_consulta DESC;
        """
    ]

    conn = get_connection()
    cur = conn.cursor()

    for query in y:
        cur.execute(query)
        resultados = cur.fetchall()
        for r in resultados:
            print(f"Data: {r[0]}, Médico: {r[1]}, Prontuário: {r[2]}")

    conn.close()