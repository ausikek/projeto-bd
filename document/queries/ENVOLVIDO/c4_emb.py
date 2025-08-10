from pymongo.database import Database

def scenery_4(db: Database):
    """4) um documento embutindo vários documentos"""
    ## Consulta: Quais os nomes dos presos envolvidos na ocorrência com id 404?

    ocorrencias = db.ocorrencias

    # Limpando as coleções

    ocorrencias.drop()

    ocorrencias.insert_one({
        "_id": 404,
        "descricao": "Homicídio",
        "cod": "D4",
        "presos": [
            {"_id": "88888888888", "nome": "Pedro"},
            {"_id": "99999999999", "nome": "Lucas"}
        ]
    })

    doc = ocorrencias.find_one({"_id": 404}, {"_id": 0, "presos.nome": 1})
    nomes = [p["nome"] for p in doc.get("presos", [])]

    print("Presos envolvidos na ocorrência com id 404;")
    for nome in nomes:
        print(nome)
