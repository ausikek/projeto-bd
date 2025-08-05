#executar insert

# imports
import sqlite3
from database.connection import get_connection
from database.inserts import inserts, insert_queries, updates

def execute_inserts():
    conn = None
    try:
        # Conecta ao banco de dados usando a função do connection.py
        conn = get_connection()
        cursor = conn.cursor()

        # Itera sobre o dicionário de inserts e executa as queries
        for table_name, data_list in inserts.items():
            query = insert_queries.get(table_name)
            if query and data_list:
                print(f"Inserindo dados na tabela {table_name}...")
                print(query, data_list)
                cursor.executemany(query, data_list)
                print(f"{cursor.rowcount} linhas inseridas em {table_name}.")
            else:
                print(f"Aviso: Não há dados ou query para a tabela {table_name}.")

        for cpf, presidio_cod in updates:
            print(f"Atualizando funcionário com CPF {cpf} para o presidio_cod {presidio_cod}...")
            cursor.execute(
                "UPDATE FUNCIONARIO SET presidio_cod = ? WHERE cpf = ?",
                (presidio_cod, cpf)
            )

        # Confirma as alterações no banco de dados
        conn.commit()
        print("Inserções concluídas com sucesso.")

    except sqlite3.Error as e:
        print(f"Erro ao inserir dados: {e}")
        if conn:
            conn.rollback()  # Desfaz as alterações em caso de erro

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    execute_inserts()