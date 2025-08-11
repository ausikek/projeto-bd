from pymongo.database import Database

def scenery_2(db: Database):
    """2) um documento embutindo apenas um documento"""
    # Consulta: Quais ocorrências foram reportadas pelo agente de cpf 22222222222?

    ocorrencias = db.ocorrencias

    ocorrencias.drop()

    # Inserindo ocorrências com agente embutido
    ocorrencias.insert_many([
        {
            "_id": 1,
            "descricao": "Apreensão de objeto ilícito",
            "agente": {
                "_id": "22222222222",
                "nome": "Ana",
                "genero": "F"
            }
        },
        {
            "_id": 2,
            "descricao": "Briga no pátio",
            "agente": {
                "_id": "22222222222",
                "nome": "Ana",
                "genero": "F"
            }
        },
        {
            "_id": 3,
            "descricao": "Tentativa de fuga",
            "agente": {
                "_id": "33333333333",
                "nome": "Bruno",
                "genero": "M"
            }
        }
    ])

    cursor = ocorrencias.find(
        {"agente._id": "22222222222"},
        {"_id": 1, "descricao": 1}
    ).sort("_id", 1)

    resultados = list(cursor)

    print("Ocorrências reportadas pelo agente de CPF 22222222222:")
    for doc in resultados:
        print(f"CÓD {doc['_id']}: {doc['descricao']}")