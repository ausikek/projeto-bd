from pymongo.database import Database

def scenery_3(db: Database):
    """3) um documento com um array de referências para documentos"""
    ## Consulta: Quais os nomes dos presos envolvidos na ocorrência com id 303?

    presos = db.presos
    ocorrencias = db.ocorrencias

    # Limpando as coleções

    ocorrencias.drop()
    presos.drop()

    joao_id = presos.insert_one({"_id": "66666666666", "nome": "João"}).inserted_id
    maria_id = presos.insert_one({"_id": "77777777777", "nome": "Maria"}).inserted_id

    ocorrencias.insert_one({
        "_id": 303,
        "descricao": "Assalto",
        "cod": "C3",
        "presos_ids": [joao_id, maria_id]
    })

    o = ocorrencias.find_one({"_id": 303}, {"presos_ids": 1})
    cursor = presos.find({"_id": {"$in": o.get("presos_ids", [])}}, {"_id": 0, "nome": 1})
    nomes = [d["nome"] for d in cursor]
    
    print("Presos envolvidos na ocorrência com id 303;")
    for nome in nomes:
        print(nome)
