from pymongo.database import Database

def scenery_3(db: Database):
    """3) um documento com um array de referências para documentos"""
    ## Consulta: Quais os nomes dos funcionários que trabalham no presídio com id 303?

    funcionarios = db.funcionarios
    presidios = db.presidios

    # Limpando as coleções

    presidios.drop()
    funcionarios.drop()

    ana_id   = funcionarios.insert_one({"_id": "66666666666", "nome": "Ana R."}).inserted_id
    bruno_id = funcionarios.insert_one({"_id": "77777777777", "nome": "Bruno S."}).inserted_id

    presidios.insert_one({
        "_id": 303,
        "cidade": "Olinda",
        "nivel_seguranca": "Média",
        "func_ids": [ana_id, bruno_id]
    })


    p = presidios.find_one({"_id": 303}, {"func_ids": 1})
    cursor = funcionarios.find({"_id": {"$in": p.get("func_ids", [])}}, {"_id": 0, "nome": 1})
    nomes = [d["nome"] for d in cursor]
    
    print("Funcionários que trabalham no presídio com id 303;")
    for nome in nomes:
        print(nome)
