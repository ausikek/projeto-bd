from scripts.create_bd import create_tables

def intro():
    print('>> Iniciando SGPCIn...')
    create_tables()  # Cria as tabelas no banco de dados
    print('>> Iniciando SGPCIn....')
    print('>> Iniciando SGPCIn..... OK!')

    print()
    print("Seja bem vindo ao Sistema de Gestão Prisional do Centro de Informática (SGPCIn)!")

    print('''

     ░██████     ░██████  ░█████████    ░██████  ░██           
 ░██   ░██   ░██   ░██ ░██     ░██  ░██   ░██               
░██         ░██        ░██     ░██ ░██        ░██░████████  
 ░████████  ░██  █████ ░█████████  ░██        ░██░██    ░██ 
        ░██ ░██     ██ ░██         ░██        ░██░██    ░██ 
 ░██   ░██   ░██  ░███ ░██          ░██   ░██ ░██░██    ░██ 
  ░██████     ░█████░█ ░██           ░██████  ░██░██    ░██ 
                                                                                                                                               
          ''')