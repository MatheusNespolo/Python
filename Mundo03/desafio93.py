jogador = {
    'Nome': '',
    'Partidas': '',
    'Total de gols': ''
}
partidas = []
jogador['Nome'] = str(input('Digite o nome: '))
jogador['Partidas'] = int(input('Quantas partidas no campeonato? '))
for i in range(0, jogador['Partidas']):
    gols = partidas.append(int(input(f'Gols na partida {i+1}: ')))
jogador['Total de gols'] = sum(partidas)
for k,v in jogador.items():
    print(f'{k}: {v}')
