#Quadrado Mágico 3x3
#https://neps.academy/br/exercise/198

linhas = []
linha1 = []
linha2 = []
linha3 = []
quadrado_magico = bool

def forma_linhas():
    for _ in range(3):
        linha1.append(int(input()))
    for _ in range(3):
        linha2.append(int(input()))
    for _ in range(3):
        linha3.append(int(input()))
    if sum(linha1) != sum(linha2) != sum(linha3):
        quadrado_magico = False
    else:
        quadrado_magico = True
    return quadrado_magico

linhas.append(linha1)
linhas.append(linha2)
linhas.append(linha3)

def forma_colunas():
    coluna1 = []
    coluna2 = []
    coluna3 = []
    for i in range(3):
        coluna1.append(linhas[i][0])
    for i in range(3):
        coluna2.append(linhas[i][1])
    for i in range(3):
        coluna3.append(linhas[i][2])
    if sum(coluna1) != sum(coluna2) != sum(coluna3):
        quadrado_magico = False
    else:
        quadrado_magico = True
    return quadrado_magico

def verifica_diagonais():
    diagonal_principal = []
    diagonal_secundaria = []
    for i in range(3):
        diagonal_principal.append(linhas[i][i])
    for i in range(3):
        diagonal_secundaria.append(linhas[i][2-i])
    if sum(diagonal_principal) != sum(diagonal_secundaria):
        quadrado_magico = False
    else:
        quadrado_magico = True
    return quadrado_magico

quadrado_magico = forma_linhas() and forma_colunas() and verifica_diagonais()

if quadrado_magico == True:
    print('SIM')
else:
    print('NAO')
