from pymongo.database import Database

def scenery_3(db: Database):
    """3) um documento com um array de referências para documentos"""
    ## Consulta: Quais as celas e suas lotações para o presídio com id 303?

    celas = db.celas
    presidios = db.presidios

    # Limpando as coleções

    presidios.drop()
    celas.drop()

    cela1_id   = celas.insert_one({"_id": "1", "lotacao_max":15 , "lotacao_atual":9}).inserted_id
    cela2_id   = celas.insert_one({"_id": "2", "lotacao_max":10 , "lotacao_atual":8}).inserted_id

    presidios.insert_one({
        "_id": 303,
        "cidade": "Olinda",
        "nivel_seguranca": "Média",
        "celas_ids": [cela1_id, cela2_id]
    })


   

    p = presidios.find_one({"_id": 303}, {"celas_ids": 1})
    cursor = celas.find({"_id": {"$in": p.get("celas_ids", [])}}, {"_id": 1, "lotacao_max": 1, "lotacao_atual": 1})

    celas_encontradas = list(cursor)

    print(f"Celas que pertencem ao presídio com id {p['_id']}:")
    for cela in celas_encontradas:
        print(f"  - Cela ID: {cela['_id']}, Lotação: {cela['lotacao_atual']}/{cela['lotacao_max']}")
