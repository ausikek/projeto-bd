from database.connection import get_connection

def subconsulta_escalar():
    """
    Executa uma subconsulta escalar que retorna o código do presídio com a maior lotação atual.
    """
    print("Executando subconsulta escalar para obter o código do presídio com a maior lotação atual...")

    # A consulta SQL que retorna o código do presídio com a maior lotação atual

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
            print(r[0])  # Imprime o código do presídio

    conn.close()