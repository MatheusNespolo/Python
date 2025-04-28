#Substituir o Maior em Matriz 3x3
#https://neps.academy/br/exercise/202

linha1 = []
linha2 = []
linha3 = []

#Função para formar as linhas
def forma_linhas():
    for _ in range(3):
        linha1.append(int(input()))
    for _ in range(3):
        linha2.append(int(input()))
    for _ in range(3):
        linha3.append(int(input()))
    return linha1, linha2, linha3

forma_linhas()

maior_valor = max(max(linha1),
                  max(linha2),
                  max(linha3))

#Substituição do maior valor da matriz
for i in range(3):
    if linha1[i] == maior_valor:
        linha1[i] = -1
    if linha2[i] == maior_valor:
        linha2[i] = -1
    if linha3[i] == maior_valor:
        linha3[i] = -1

print(*linha1)
print(*linha2)
print(*linha3)
