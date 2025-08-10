from pymongo.database import Database

def scenery_1(db: Database):
    """1) um documento referenciando apenas um documento"""
    ## Consulta: Quais são os nomes dos médicos que realizaram consultas na data 2025-01-10?

    medicos = db.medicos
    consultas = db.consultas

    # Limpando as coleções

    consultas.drop()
    medicos.drop()

    medicos.insert_many([
    {"_id": "11111111111", #cpf
    "nome": "Dr. João C.",
    "cod_crm": "12345"},

    {"_id": "22222222222", #cpf
    "nome": "Dr. Bernardo B.",
    "cod_crm": "67809"},
])

    consultas.insert_many([
        {"_id": "C1 2025-01-10", #identificador do mongodb
         "data": "2025-01-10", 
         "prontuario": "Paciente com febre", 
         "medico_cpf": "11111111111"},

        {"_id": "C2 2025-10-01", #identificador do mongodb
         "data": "2025-10-01", 
         "prontuario": "Paciente com lesões no corpo", 
         "medico_cpf": "22222222222"}
    ])

    cons = consultas.find_one({"data": "2025-01-10"})
    
    if cons:
        print(f"Consultas encontradas: {cons['_id']} com médico de cpf {cons['medico_cpf']}")
    else:
        print("Não há consultas nessa data.")

    cursor = medicos.find({"_id": cons["medico_cpf"]}, {"_id": 0, "nome": 1})

    nomes = [d["nome"] for d in cursor]
    
    print("Médicos que realizaram consultas na data 2025-01-10:")
    for nome in nomes:
        print(nome)
