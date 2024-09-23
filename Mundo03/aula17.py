valores = list()
for cont in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Final da lista.')

b = valores[:]
b[3] = 8
print(b)