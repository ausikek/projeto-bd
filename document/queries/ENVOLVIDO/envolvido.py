from document.connection import get_mongo_client
from document.queries.ENVOLVIDO.c1_ref import scenery_1
from document.queries.ENVOLVIDO.c2_emb import scenery_2
from document.queries.ENVOLVIDO.c3_ref import scenery_3
from document.queries.ENVOLVIDO.c4_emb import scenery_4

def envolvido():
    client = get_mongo_client()
    db = client["sistema_penal"]

    print('''
Escolha a consulta que deseja executar:
1 - Consulta: Documento que referencia outro documento
2 - Consulta: Documento que embute apenas um documento
3 - Consulta: Documento com um array de referências para outro documento
4 - Consulta: Documento que embute varios documentos
r - Retornar
          ''')
    
    sentinel = True
    
    while sentinel:
        query_number = input("~$ ")
        if query_number == '1':
            scenery_1(db)
        elif query_number == '2':
            scenery_2(db)
        elif query_number == '3':
            scenery_3(db)
        elif query_number == '4':
            scenery_4(db)
        elif query_number == 'r':
            sentinel = False
        else:
            print("Número de consulta inválido. Escolha entre 1 e 4.")
