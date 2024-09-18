precos = nomes = []
precos = [int(x) for x in precos]
sair = bool = False
soma = caro = 0
while not sair:
    nome = str(input('Nome do produto: '))
    nomes.append(nome)
    preco = float(input('Preço do produto: '))
    precos.append(preco)
    if preco > 1000:
        caro += 1
    soma += preco
    cont = str(input('Continuar? (S/N) '))
    if cont in 'Nn':
        sair == True
        break
    elif cont in 'Ss':
        sair == False
    else:
        sair == True
        break
barato = min(precos)
indice = precos.index(barato)
print(f'a) {soma}\nb) {caro}\nc) {nomes[indice]}')