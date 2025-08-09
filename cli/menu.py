from cli.main_loop_sql import loop_sql
from cli.main_loop_mongo import loop_mongo
from cli.loop_choices import choices

def menu():
    choice = int(input("~$ "))

    sentinel = True

    while sentinel:
        if choice == 0:
            sentinel = False
            
            print("Saindo do SGPCIn. Até logo...")            
        elif choice == 1:
            loop_sql()
            choices()
            choice = int(input("~$ "))
        elif choice == 2:
            loop_mongo()
            choices()
            choice = int(input("~$ "))
        else:
            print("Opção inválida.")
            choices()
            choice = int(input("~$ "))