#Positivos e Média
soma = 0
positivos = 0
for i in range (0,6):
    num = float(input())
    if num > 0:
        positivos += 1
        soma += num
print(f'{positivos} valores positivos')
print(f'{soma/positivos:.1f}')
