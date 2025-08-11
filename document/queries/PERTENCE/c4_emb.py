from pymongo.database import Database

def scenery_4(db: Database):
    """4) um documento embutindo vários documentos"""
    ## Consulta: Quais os nomes dos funcionários que trabalham no presídio com id 404?

    presidios = db.presidios

    # Limpando as coleções

    presidios.drop()

    presidios.insert_one({
    "_id": 404,
    "cidade": "Jaboatão",
    "nivel_seguranca": "Baixa",
    "funcionarios": [
        {"_id": "88888888888", "nome": "Eva"},
        {"_id": "99999999999", "nome": "Felipe"}
    ]
    })

    doc = presidios.find_one({"_id": 404}, {"_id": 0, "funcionarios.nome": 1})
    nomes = [f["nome"] for f in doc.get("funcionarios", [])]

    print("Funcionários que trabalham no presídio com id 404;")
    for nome in nomes:
        print(nome)
