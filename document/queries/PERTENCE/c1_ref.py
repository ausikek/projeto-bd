from pymongo.database import Database

def scenery_1(db: Database):
    """1) um documento referenciando apenas um documento"""
    ## Consulta: Quais os nomes dos funcionários que trabalham no presídio com id 101?

    funcionarios = db.funcionarios
    presidios = db.presidios

    # Limpando as coleções

    presidios.drop()
    funcionarios.drop()

    presidios.insert_one({
    "_id": 101,
    "cidade": "Recife",
    "nivel_seguranca": "Alta",
    "lotacao_max": 500,
    "lotacao_atual": 350,
    "diretor_cpf": "11111111111"
})

    funcionarios.insert_many([
        {"_id": "22222222222", "nome": "Ana",   "genero": "F", "presidio_id": 101},
        {"_id": "33333333333", "nome": "Bruno", "genero": "M", "presidio_id": 101},
    ])

    p = presidios.find_one({"_id": 101})
    
    if p:
        print(f"Presídio encontrado: {p['cidade']} com id {p['_id']}")
    else:
        print("Presídio não encontrado.")

    cursor = funcionarios.find({"presidio_id": p["_id"]}, {"_id": 0, "nome": 1})

    nomes = [d["nome"] for d in cursor]
    
    print("Funcionários que trabalham no presídio com id 101;")
    for nome in nomes:
        print(nome)
