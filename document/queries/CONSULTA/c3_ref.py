from pymongo.database import Database

def scenery_3(db: Database):
    """3) um documento com um array de referências para documentos"""
    ## Consulta: Quais são os nomes dos médicos que realizaram consultas na data 2025-02-06?

    medicos = db.medicos
    consultas = db.consultas

    # Limpando as coleções

    consultas.drop()
    medicos.drop()

    #id é o cpf
    breno_id = medicos.insert_one({"_id": "55555555555", "nome": "Dr. Breno F.", "cod_crm": "19285"}).inserted_id
    guilherme_id = medicos.insert_one({"_id": "66666666666", "nome": "Dr. Guilherme S.", "cod_crm": "37546"}).inserted_id

    consultas.insert_one({
        "_id": "C6 2025-02-06",
        "data": "2025-02-06",
        "prontuario": "Paciente com fratura na perna",
        "medico_ids": [breno_id, guilherme_id]
    })


    c = consultas.find_one({"data": "2025-02-06"}, {"medico_ids": 1})
    cursor = medicos.find({"_id": {"$in": c.get("medico_ids", [])}}, {"_id": 0, "nome": 1})
    nomes = [d["nome"] for d in cursor]
    
    print("Médicos que realizaram consultas na data 2025-02-06:")
    for nome in nomes:
        print(nome)
