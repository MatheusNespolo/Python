#Soma das Diagonais da Matriz 3x3
#https://neps.academy/br/exercise/201

linhas = []
linha1 = []
linha2 = []
linha3 = []

def forma_linhas():
    for _ in range(3):
        linha1.append(int(input()))
    for _ in range(3):
        linha2.append(int(input()))
    for _ in range(3):
        linha3.append(int(input()))

linhas.append(linha1)
linhas.append(linha2)
linhas.append(linha3)

def soma_diagonais():
    diagonal_principal = []
    diagonal_secundaria = []
    for i in range(3):
        diagonal_principal.append(linhas[i][i])
    for i in range(3):
        diagonal_secundaria.append(linhas[i][2-i])
    somaDiag1 = sum(diagonal_principal)
    somaDiag2 = sum(diagonal_secundaria)
    return somaDiag1, somaDiag2


forma_linhas()
saida = (soma_diagonais())
print('Diagonal principal: ' + str(saida[0]))
print('Diagonal secundaria: ' + str(saida[1]))
