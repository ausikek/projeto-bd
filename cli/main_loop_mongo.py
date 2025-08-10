from document.queries.TRABALHA.trabalha import trabalha

def loop_mongo_choices():
    print('''
1 - Relacionamento TRABALHA (Nome dos funcionários que trabalham no presídio)
2 - TODO
3 - TODO
4 - TODO
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
            print("Opção 2 ainda não implementada.")
        elif choice == '3':
            print("Opção 3 ainda não implementada.")
        elif choice == '4':
            print("Opção 4 ainda não implementada.")
        elif choice == '5':
            print("Opção 5 ainda não implementada.")
        elif choice == 'r':
            sentinel = False
        else:
            print('Opção inválida. Tente novamente.')