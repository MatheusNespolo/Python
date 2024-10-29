def ficha(nome = '', gols = ''):
    if nome == '':
        nome = '<desconhecido>'
    if gols == '':
        gols = '0'
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

njogador = str(input('Nome do jogador: '))
ngols = str(input('Gols no campeonato: '))
ficha(njogador, ngols)
