#Soma das Colunas de Matriz 3x3
#https://neps.academy/br/exercise/200

#Entrada
coluna0 = []
coluna1 = []
coluna2 = []

for i in range(3):
    coluna0.append(int(input()))
    coluna1.append(int(input()))
    coluna2.append(int(input()))

#Processamento
soma0 = sum(coluna0)
soma1 = sum(coluna1)
soma2 = sum(coluna2)

#Saída
print(f'Coluna 0: {soma0}')
print(f'Coluna 1: {soma1}')
print(f'Coluna 2: {soma2}')
