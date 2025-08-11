from pymongo.database import Database

def scenery_2_corrected(db: Database):
    """2) um documento embutindo apenas um documento"""
    ## Consulta: Quais as lotações das celas que pertencem ao presídio com id 202?

    celas = db.celas

    # Limpando as coleções
    celas.drop()

    # Inserindo documentos de "cela", cada um embutindo o mesmo documento de "presidio"
    # (Isso demonstra o padrão, mas não é um modelo de dados recomendado para produção)
    celas.insert_many([
    {
        "_id": "C101", 
        "lotacao_max": 10,
        "lotacao_atual": 3,
        "presidio": {"_id": 202, "cidade": "Recife", "nivel_seguranca": "Alta", "lotacao_max": 500, "lotacao_atual": 350, "diretor_cpf": "11111111111"}
    },
    {
        "_id": "C102", 
        "lotacao_max": 15,
        "lotacao_atual": 9,
        "presidio": {"_id": 202, "cidade": "Recife", "nivel_seguranca": "Alta", "lotacao_max": 500, "lotacao_atual": 350, "diretor_cpf": "11111111111"}
    }
    ])

    
    cursor = celas.find({"presidio._id": 202}, {"_id": 1, "lotacao_max": 1,"lotacao_atual": 1})
    celas_encontradas = list(cursor)

    
    print(f"Celas que pertencem ao presídio com id 202:")
    for cela in celas_encontradas:
        
        print(f"  - Cela ID: {cela['_id']}, Lotação: {cela['lotacao_atual']}/{cela['lotacao_max']}")