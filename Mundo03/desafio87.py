linha1 = []
linha2 = []
linha3 = []
matriz = [linha1, linha2, linha3]
somap = 0
soma3 = 0
for i in range(0,9):
    if i >= 0 and i <= 2:
        linha1.append(int(input(f'Valor para [0, {i}]: ')))
    elif i > 2 and i <= 5:
        linha2.append(int(input(f'Valor para [1, {i-3}]: ')))
    elif i > 5 and i <= 9:
        linha3.append(int(input(f'Valor para [2, {i-6}]: ')))
for i in linha1:
    if i % 2 == 0:
        somap += i
for i in linha2:
    if i % 2 == 0:
        somap += i
for i in linha3:
    if i % 2 == 0:
        somap += i
for i in linha3:
    soma3 += i
for linha in matriz:
    print(linha)
print(f'A soma dos valores pares da matriz é {somap}')
print(f'A soma dos valores da terceira linha é {soma3}')
