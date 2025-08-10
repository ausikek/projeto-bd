from document.queries.REPORTA.reporta import reporta
from document.queries.TRABALHA.trabalha import trabalha
from document.queries.CONSULTA.consulta import consulta
from document.queries.ENVOLVIDO.envolvido import envolvido

def loop_mongo_choices():
    print('''
1 - Relacionamento TRABALHA (Nome dos funcionários que trabalham no presídio)
2 - Relacionamento CONSULTA (Nome dos médicos que atenderam na data)
3 - Relacionamento ENVOLVIDO (Nome dos envolvidos na ocorrência)
4 - Relacionamento REPORTA (Nome das ocorrências reportadas por um agente)
5 - TODO
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
            print("Opção 5 ainda não implementada.")
        elif choice == 'r':
            sentinel = False
        else:
            print('Opção inválida. Tente novamente.')