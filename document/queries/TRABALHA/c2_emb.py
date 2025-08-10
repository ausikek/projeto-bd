from pymongo.database import Database

def scenery_2(db: Database):
    """2) um documento embutindo apenas um documento"""
    ## Consulta: Quais os nomes dos funcionários que trabalham no presídio com id 202?

    funcionarios = db.funcionarios

    # Limpando as coleções
    
    funcionarios.drop()

    funcionarios.insert_many([
    {
        "_id": "44444444444",
        "nome": "Carla",
        "presidio": {"_id": 202, "cidade": "Recife", "nivel_seguranca": "Alta", "lotacao_max": 500, "lotacao_atual": 350, "diretor_cpf": "11111111111"}
    },
    {
        "_id": "55555555555",
        "nome": "Diego",
        "presidio": {"_id": 202, "cidade": "Recife", "nivel_seguranca": "Alta", "lotacao_max": 500, "lotacao_atual": 350, "diretor_cpf": "11111111111"}
    }
    ])

    cursor = funcionarios.find({"presidio._id": 202}, {"_id": 0, "nome": 1})
    nomes = [d["nome"] for d in cursor]
    
    print("Funcionários que trabalham no presídio com id 202;")
    for nome in nomes:
        print(nome)
 
