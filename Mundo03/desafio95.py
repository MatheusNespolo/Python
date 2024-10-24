jogador = {
    'Nome': '',
    'Partidas': '',
    'Total de gols': ''
}
partidas = []
time = []

while True:
    jogador.clear()
    jogador['Nome'] = str(input('Digite o nome: '))
    jogador['Partidas'] = int(input('Quantas partidas no campeonato? '))
    partidas.clear()
    for i in range(0, jogador['Partidas']):
        gols = partidas.append(int(input(f'Gols na partida {i + 1}: ')))
    jogador['gols'] = partidas[:]
    jogador['Total de gols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? (S/N) ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Jogador não cadastrado.')
    else:
        print(f'Dados de {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f' No jogo {i+1} fez {g} gols.')
