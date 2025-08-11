from document.queries.REPORTA.reporta import reporta
from document.queries.TRABALHA.trabalha import trabalha
from document.queries.CONSULTA.consulta import consulta
from document.queries.ENVOLVIDO.envolvido import envolvido
from document.queries.PERTENCE.pertence import pertence

def loop_mongo_choices():
    print('''
1 - Relacionamento TRABALHA (Nome dos funcionários que trabalham no presídio)
2 - Relacionamento CONSULTA (Nome dos médicos que atenderam na data)
3 - Relacionamento ENVOLVIDO (Nome dos envolvidos na ocorrência)
4 - Relacionamento REPORTA (Nome das ocorrências reportadas por um agente)
5 - Relacionamento PERTENCE (Lotação das celas que pertencem ao presídio)
r - Retornar
            ''')

def loop_mongo():
    loop_mongo_choices()
    
    sentinel = True

    while sentinel:
        choice = input("~$ ")
        if choice == '1':
            trabalha()
            loop_mongo_choices()

        elif choice == '2':
            consulta()
            loop_mongo_choices()

        elif choice == '3':
            envolvido()
            loop_mongo_choices()

        elif choice == '4':
            reporta()
            loop_mongo_choices()

        elif choice == '5':
            pertence()
            loop_mongo_choices()

        elif choice == 'r':
            sentinel = False
        else:
            print('Opção inválida. Tente novamente.')