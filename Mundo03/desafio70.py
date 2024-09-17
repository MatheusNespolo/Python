sair = bool = False
soma = caro = 0
while not sair:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    if preco > 1000:
        caro +=1
    soma += preco
    cont = str(input('Continuar? (S/N) '))
    if cont in 'Nn':
        sair == True
    elif cont in 'Ss':
        sair == False
    else:
        sair == True
print(f'a) {soma}\nb) {}')