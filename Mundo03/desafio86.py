linha1 = []
linha2 = []
linha3 = []
for i in range(0,9):
    if i >= 0 and i <= 2:
        linha1.append(int(input(f'Valor para [0, {i}]: ')))
    elif i > 2 and i <= 5:
        linha2.append(int(input(f'Valor para [1, {i-3}]: ')))
    elif i > 5 and i <= 9:
        linha3.append(int(input(f'Valor para [2, {i-6}]: ')))
print(linha1)
print(linha2)
print(linha3)