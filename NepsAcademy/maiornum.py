#Desafio do Maior Número

sequencia = list(map(int, input().split()))

sequencia.pop(len(sequencia) - 1)

print(max(sequencia))
