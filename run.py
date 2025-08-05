from scripts.create_bd import create_tables
from scripts.exec_ins import execute_inserts

if __name__ == "__main__":
    create_tables()  # Cria as tabelas no banco de dados
    execute_inserts()  # Executa os inserts nas tabelas criadas