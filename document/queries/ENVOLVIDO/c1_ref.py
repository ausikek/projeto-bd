from pymongo.database import Database

def scenery_1(db: Database):
    """1) um documento referenciando apenas um documento"""
    ## Consulta: Quais os nomes dos presos envolvidos na ocorrência com id 101?

    presos = db.presos
    ocorrencias = db.ocorrencias

    # Limpando as coleções

    ocorrencias.drop()
    presos.drop()

    ocorrencias.insert_one({
        "_id": 101,
        "descricao": "Fuga",
        "cod": "A1"
    })

    presos.insert_many([
        {"_id": "22222222222", "nome": "João", "ocorrencia_id": 101},
        {"_id": "33333333333", "nome": "Maria", "ocorrencia_id": 101},
    ])

    o = ocorrencias.find_one({"_id": 101})
    
    if o:
        print(f"Ocorrência encontrada: {o['descricao']} com id {o['_id']}")
    else:
        print("Ocorrência não encontrada.")

    cursor = presos.find({"ocorrencia_id": o["_id"]}, {"_id": 0, "nome": 1})

    nomes = [d["nome"] for d in cursor]
    
    print("Presos envolvidos na ocorrência com id 101;")
    for nome in nomes:
        print(nome)
