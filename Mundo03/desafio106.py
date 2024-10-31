import colorama
from time import sleep

def ajuda(com):
    print(colorama.Fore.CYAN + f'Acessando manual do comando: {com}' + colorama.Style.RESET_ALL)
    sleep(1.5)
    help(com)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(colorama.Back.RED + '~'*tam + colorama.Style.RESET_ALL)
    print(colorama.Back.RED + f'  {msg}  ' + colorama.Style.RESET_ALL)
    print(colorama.Back.RED + '~'*tam + colorama.Style.RESET_ALL)

comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO')
