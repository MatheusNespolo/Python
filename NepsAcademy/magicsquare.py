#Quadrado Mágico 3x3
#https://neps.academy/br/exercise/198

linhas = []

for i in range(9):
    linha1 = []
    linha2 = []
    linha3 = []
    if i <= 3:
        linha1.append(int(input()))
    if i > 3 and i <= 6:
        linha2.append(int(input()))