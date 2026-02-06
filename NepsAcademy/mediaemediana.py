#Média e mediana

# https://neps.academy/br/exercise/1656

# A média de três números inteiros A, B e C é (A + B + C)/3. A mediana de três npúmeros inteiros é o número que ficaria no meio se os três números fossem ordenados em ordem crescente.

# Sua tarefa é escrever um programa que, dados dois números inteiros distintos A e B, calcule o menor inteiro possível C tal que a média e a mediana de A, B e C sejam iguais. 

# Entrada
A, B = map(int, input().split())

C = 0

# Processamento
media = (A + B + C) / 3

mediana = (sorted([A, B, C]))[1]

while media != mediana:
    if mediana > media:
        C -= 1
    else:
        C += 1
        media = (A + B + C) / 3
        mediana = (sorted([A, B, C]))[1]


# Saída - deve produzir uma única linha, contendo um único número, o menor inteiro possível C tal que a média e a mediana de A, B e C sejam iguais.

print(C)
