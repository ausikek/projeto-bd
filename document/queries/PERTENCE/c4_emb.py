from pymongo.database import Database

def scenery_4(db: Database):
    """4) um documento embutindo vários documentos"""

    presidios = db.presidios

    # Limpando as coleções
    presidios.drop()

    # Inserindo presídio com documentos embutidos no campo 'celas'
    presidios.insert_one({
        "_id": 404,
        "cidade": "Jaboatão",
        "nivel_seguranca": "Baixa",
        "celas": [
            {"_id": "22222222222", "lotacao_max": 10, "lotacao_atual": 3},
            {"_id": "33333333333", "lotacao_max": 20, "lotacao_atual": 16}
        ]
    })

    # Consulta
    doc = presidios.find_one(
        {"_id": 404},
        {"_id": 0, "celas._id": 1, "celas.lotacao_max": 1, "celas.lotacao_atual": 1}
    )

    print("Celas que pertencem ao presídio com id 404:")
    for cela in doc.get("celas", []):
        print(f"  - Cela ID: {cela['_id']}, Lotação: {cela['lotacao_atual']}/{cela['lotacao_max']}")
