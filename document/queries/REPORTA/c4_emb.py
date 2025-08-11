from pymongo.database import Database

def scenery_4(db: Database):
    """4) um documento embutindo vários documentos"""
    # Consulta: Quais ocorrências foram reportadas pelo agente de cpf 22222222222?

    agentes= db.agentes
    agentes.drop()

    # Inserindo agente com várias ocorrências embutidas
    agentes.insert_one({
        "_id": "22222222222",
        "nome": "Ana",
        "genero": "F",
        "ocorrencias": [
            {"_id": 1, "descricao": "Apreensão de objeto ilícito"},
            {"_id": 2, "descricao": "Briga no pátio"}
        ]
    })

    # Outro agente apenas para diferenciar
    agentes.insert_one({
        "_id": "33333333333",
        "nome": "Bruno",
        "genero": "M",
        "ocorrencias": [
            {"_id": 3, "descricao": "Tentativa de fuga"}
        ]
    })

    # consulta pelo CPF e retorno das ocorrências embutidas
    doc = agentes.find_one({"_id": "22222222222"}, {"_id": 0, "ocorrencias": 1})
    ocorrencias = doc.get("ocorrencias", [])

    print("Ocorrências reportadas pelo agente de CPF 22222222222:")
    for oc in ocorrencias:
        print(f"CÓD {oc['_id']}: {oc['descricao']}")