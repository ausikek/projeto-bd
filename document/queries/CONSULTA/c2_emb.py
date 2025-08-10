from pymongo.database import Database

def scenery_2(db: Database):
    """2) um documento embutindo apenas um documento"""
    ## Consulta: Quais são os nomes dos médicos que realizaram consultas na data 2025-08-09?


    consultas = db.consultas

    # Limpando as coleções
    
    consultas.drop()

    consultas.insert_many([
    {
        "_id": "C3 2025-08-09",
        "data": "2025-08-09",
        "prontuario": "Paciente com apendicite",
        "medico": {"_id": "33333333333", "nome": "Dr. Diego P.", "cod_crm": "20468"}
    },
    {
        "_id": "C4 2025-08-09",
        "data": "2025-08-09",
        "prontuario": "Paciente com dores de cabeça",
        "medico": {"_id": "44444444444", "nome": "Dr. Carlos R.", "cod_crm": "13579"}
    },
    {
        "_id": "C5 2025-03-04",
        "data": "2025-03-04",
        "prontuario": "Paciente com sintomas de gripe",
        "medico": {"_id": "99999999999", "nome": "Dr. Gabriel G.", "cod_crm": "13579"}
    }
    ])

    cursor = consultas.find({"data": "2025-08-09"}, {"_id": 0, "medico": 1})
    nomes = [d["medico"]["nome"] for d in cursor]
    
    print("Médicos que realizaram consultas na data 2025-08-09:")
    for nome in nomes:
        print(nome)
 
