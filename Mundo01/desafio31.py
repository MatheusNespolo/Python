dist = float(input('Digite a distância da viagem (Km): '))
if dist <= 200:
    preco = dist * 0.5
else:
    preco = dist * 0.45
print('O preço da viagem é', preco)