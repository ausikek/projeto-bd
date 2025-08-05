from scripts.exec_ins import execute_inserts
from database.queries.subconsulta_escalar import subconsulta_escalar
from database.queries.subconsulta_linha import subconsulta_linha

def loop():
    print('''
0 - Semear o banco de dados
1 - Consulta: anti-join
2 - Consulta: subconsulta escalar
3 - Consulta: subconsulta de linha
4 - Consulta: subconsulta de tabela
5 - Consulta: group-by
6 - Consulta: inner-join
7 - Consulta: left-join
8 - Consulta: semi-join
9 - Consulta: union
q - Sair
          ''')

    while True:
        choice = input('Escolha uma opção: ')
        if choice == '0':
            execute_inserts()
        elif choice == '1':
            #anti_join()
            print("Anti-join não implementado.")
        elif choice == '2':
            subconsulta_escalar()
        elif choice == '3':
            subconsulta_linha()
        elif choice == '4':
            #table_subquery()
            print("Subconsulta de tabela não implementada.")    
        elif choice == '5':
            #group_by()
            print("Group by não implementado.")
        elif choice == '6':
            #inner_join()
            print("Inner join não implementado.")
        elif choice == '7':
            #left_join()
            print("Left join não implementado.")
        elif choice == '8':
            #semi_join()
            print("Semi join não implementado.")
        elif choice == '9':
            #union()
            print("Union não implementado.")
        elif choice == 'q':
            print("Saindo do SGPCIn. Até logo...")
            break
        else:
            print('Opção inválida. Tente novamente.')
