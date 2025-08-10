from pymongo.database import Database

def scenery_2(db: Database):
    """2) um documento embutindo apenas um documento"""
    ## Consulta: Quais os nomes dos presos envolvidos na ocorrência com id 202?

    presos = db.presos

    # Limpando as coleções
    
    presos.drop()

    presos.insert_many([
        {
            "_id": "44444444444",
            "nome": "Carlos",
            "ocorrencia": {"_id": 202, "descricao": "Roubo", "cod": "B2"}
        },
        {
            "_id": "55555555555",
            "nome": "Ana",
            "ocorrencia": {"_id": 202, "descricao": "Roubo", "cod": "B2"}
        }
    ])

    cursor = presos.find({"ocorrencia._id": 202}, {"_id": 0, "nome": 1})
    nomes = [d["nome"] for d in cursor]
    
    print("Presos envolvidos na ocorrência com id 202;")
    for nome in nomes:
        print(nome)
