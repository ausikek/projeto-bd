from cli.healthcheck import healthcheck
from cli.loop_choices import choices


def intro():
    print('>> Iniciando SGPCIn...')
    healthy = healthcheck()

    if healthy:
        print('>> Iniciando SGPCIn.... OK!\n')

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
        
        choices()
    
    else:
        print('>> Iniciando SGPCIn.... ERRO!')
        print('>> O sistema não está pronto para uso. Verifique os logs para mais detalhes.')
        print('>> Encerrando SGPCIn...')
        exit(1)