#Quadrado Mágico 3x3
#https://neps.academy/br/exercise/198

#Entrada
linha0 = []
linha1 = []
linha2 = []
coluna0 = []
coluna1 = []
coluna2 = []

for i in range(3):
    linha0.append(int(input()))
for i in range(3):
    linha1.append(int(input()))
for i in range(3):
    linha2.append(int(input()))
coluna0.append(linha0[0])
coluna0.append(linha1[0])
coluna0.append(linha2[0])
coluna1.append(linha0[1])
coluna1.append(linha1[1])
coluna1.append(linha2[1])
coluna2.append(linha0[2])
coluna2.append(linha1[2])
coluna2.append(linha2[2])

#Processamento
soma0 = sum(linha0)
soma1 = sum(linha1)
soma2 = sum(linha2)

#Saída
print(f'Linha 0: {soma0}')
print(f'Linha 1: {soma1}')
print(f'Linha 2: {soma2}')
