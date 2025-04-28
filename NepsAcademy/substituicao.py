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

#Sugestão trabalhando com matriz

# # Lendo a matriz como uma lista de listas
# matriz = [ [int(input()) for _ in range(3)] for _ in range(3) ]

# # Encontrando o maior valor
# maior_valor = max(max(linha) for linha in matriz)

# # Substituindo todas as ocorrências
# for i in range(3):
#     for j in range(3):
#         if matriz[i][j] == maior_valor:
#             matriz[i][j] = -1

# # Imprimindo
# for linha in matriz:
#     print(*linha)

