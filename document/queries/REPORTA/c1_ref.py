from pymongo.database import Database

def scenery_1(db: Database):
    """1) um documento referenciando apenas um documento"""
    # Consulta: Quais ocorrências foram reportadas pelo agente de cpf 22222222222?

    ocorrencias = db.ocorrencias
    agentes = db.agentes

    # Limpando
    agentes.drop()
    ocorrencias.drop()

    agentes.insert_one({
        "_id": "22222222222", 
        "nome": "Ana",   
        "genero": "F", 
    })

    ocorrencias.insert_many([
        {"_id": 1, "descricao": "Apreensão de objeto ilícito", "agente_cpf": "22222222222"},
        {"_id": 2, "descricao": "Briga no pátio", "agente_cpf": "22222222222"},
        {"_id": 3, "descricao": "Tentativa de fuga", "agente_cpf": "33333333333"},
    ])

    ag = agentes.find_one({"_id": "22222222222"})
    if ag:
        print(f"Agente encontrado: {ag['nome']} com CPF {ag['_id']}")
    else:
        print("Agente não encontrado.")

    cursor = ocorrencias.find(
        {"agente_cpf": ag["_id"]},
        {"_id": 1, "descricao": 1}
    ).sort("_id", 1)
    resultados = list(cursor)

    print("Ocorrências reportadas pelo agente de CPF 22222222222:")
    for doc in resultados:
        print(f"CÓD {doc['_id']}: {doc['descricao']}")