#  Plantação de Morangos
#  https://neps.academy/br/exercise/53

# Entrada
dados = []
for i in range(4):
    n = int(input())
    dados.append(n)
 
# Processamento
area1 = dados[0] * dados[1]
area2 = dados[2] * dados[3]
maiorArea = (max(area1, area2))

# Saída
print(maiorArea)
