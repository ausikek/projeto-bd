#executar insert

# imports
import sqlite3
from ..database.connection import db_connection
from ..database.inserts import inserts, insert_queries

def execute_inserts():
    conn = None
    try:
        # Conecta ao banco de dados usando a função do connection.py
        conn = db_connection()
        cursor = conn.cursor()

        # Itera sobre o dicionário de inserts e executa as queries
        for table_name, data_list in inserts.items():
            query = insert_queries.get(table_name)
            if query and data_list:
                print(f"Inserindo dados na tabela {table_name}...")
                cursor.executemany(query, data_list)
                print(f"{cursor.rowcount} linhas inseridas em {table_name}.")
            else:
                print(f"Aviso: Não há dados ou query para a tabela {table_name}.")

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