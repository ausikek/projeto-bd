from pymongo.database import Database

def scenery_1(db: Database):
    """1) um documento referenciando apenas um documento
    Consulta: Quais as celas que pertencem ao presídio com id 101?
    """

    presidios = db.presidios
    celas = db.celas

    # Limpando as coleções
    celas.drop()
    presidios.drop()

    # Inserindo presídio
    presidios.insert_one({
        "_id": 101,
        "cidade": "Recife",
        "nivel_seguranca": "Alta",
        "lotacao_max": 500,
        "lotacao_atual": 350,
        "diretor_cpf": "11111111111"
    })

    # Inserindo celas (sem nome)
    celas.insert_many([
        {"_id": "22222222222", "lotacao_max": 10, "lotacao_atual": 3, "presidio_id": 101},
        {"_id": "33333333333", "lotacao_max": 15, "lotacao_atual": 9, "presidio_id": 101},
    ])

    # Buscar presídio
    p = presidios.find_one({"_id": 101})
    if not p:
        print("Presídio não encontrado.")
        return
    else:
        print(f"Presídio encontrado: {p['cidade']} com id {p['_id']}")

    # Buscar celas do presídio (mostrando id e lotação)
    cursor = celas.find({"presidio_id": p["_id"]}, {"_id": 1, "lotacao_max": 1, "lotacao_atual": 1})

    print("Celas que pertencem ao presídio com id 101:")
    for cela in cursor:
        print(f"Cela ID: {cela['_id']}, Lotação: {cela['lotacao_atual']}/{cela['lotacao_max']}")
