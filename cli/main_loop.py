from scripts.exec_ins import execute_inserts
from database.queries.subconsulta_escalar import subconsulta_escalar
from database.queries.subconsulta_linha import subconsulta_linha
from database.queries.groupby import groupby_query
from database.queries.inner_join import inner_join_query
from database.queries.left_join import left_join_query
from database.queries.table_subquery import table_subquery
from database.queries.union_query import union_query
from database.queries.semi_join import semi_join_query
from database.queries.anti_join import anti_join_query

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
            anti_join_query()
        elif choice == '2':
            subconsulta_escalar()
        elif choice == '3':
            subconsulta_linha()
        elif choice == '4':
            table_subquery()
        elif choice == '5':
            groupby_query()
        elif choice == '6':
            inner_join_query()
        elif choice == '7':
            left_join_query()
        elif choice == '8':
            semi_join_query()
        elif choice == '9':
            union_query()
        elif choice == 'q':
            print("Saindo do SGPCIn. Até logo...")
            break
        else:
            print('Opção inválida. Tente novamente.')
