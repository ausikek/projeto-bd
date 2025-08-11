from pymongo.database import Database

def scenery_3(db: Database):
    """3) um documento com um array de referências para documentos"""
    # Consulta: Quais ocorrências foram reportadas pelo agente de CPF 22222222222?

    ocorrencias = db.ocorrencias
    agentes = db.agentes

    agentes.drop()
    ocorrencias.drop()

    # Inserindo ocorrências e guardando seus _id
    oc1_id = ocorrencias.insert_one({
        "_id": 1,
        "descricao": "Apreensão de objeto ilícito"
    }).inserted_id

    oc2_id = ocorrencias.insert_one({
        "_id": 2,
        "descricao": "Briga no pátio"
    }).inserted_id

    oc3_id = ocorrencias.insert_one({
        "_id": 3,
        "descricao": "Tentativa de fuga"
    }).inserted_id

    # Inserindo agente com array de referências para as ocorrências
    agentes.insert_one({
        "_id": "22222222222",
        "nome": "Ana",
        "genero": "F",
        "ocorrencias_ids": [oc1_id, oc2_id]
    })

    # consultando agente e depois as ocorrências
    ag = agentes.find_one({"_id": "22222222222"}, {"ocorrencias_ids": 1})
    cursor = ocorrencias.find(
        {"_id": {"$in": ag.get("ocorrencias_ids", [])}},
        {"_id": 1, "descricao": 1}
    ).sort("_id", 1)
    resultados = list(cursor)

    print("Ocorrências reportadas pelo agente de CPF 22222222222:")
    for doc in resultados:
        print(f"CÓD {doc['_id']}: {doc['descricao']}")