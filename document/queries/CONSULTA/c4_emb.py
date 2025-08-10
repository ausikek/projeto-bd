from pymongo.database import Database

def scenery_4(db: Database):
    """4) um documento embutindo vários documentos"""
    ## Consulta: Quais são os nomes dos médicos que realizaram consultas na data 2025-05-07?

    consultas = db.consultas

    # Limpando as coleções

    consultas.drop()

    consultas.insert_one({
        "_id": "Consultas 2025-05-07",
        "data": "2025-05-07",
        "medicos": [
            {"_id": "77777777777", "nome": "Dr. Robson F.", "cod_crm": "54321"},
            {"_id": "88888888888", "nome": "Dr. Felipe C.", "cod_crm": "98765"}
        ]
    })

    doc = consultas.find_one({"data": "2025-05-07"}, {"_id": 0, "medicos.nome": 1})
    nomes = [f["nome"] for f in doc.get("medicos", [])]

    print("Médicos que realizaram consulta na data 2025-05-07:")
    for nome in nomes:
        print(nome)
