#Soma das Linhas de Matriz 3x3
#https://neps.academy/br/exercise/199

#Entrada
linha0 = []
linha1 = []
linha2 = []

for i in range(3):
    linha0.append(int(input()))
for i in range(3):
    linha1.append(int(input()))
for i in range(3):
    linha2.append(int(input()))

#Processamento
soma0 = sum(linha0)
soma1 = sum(linha1)
soma2 = sum(linha2)

#Saída
print(f'Linha 0: {soma0}')
print(f'Linha 1: {soma1}')
print(f'Linha 2: {soma2}')
