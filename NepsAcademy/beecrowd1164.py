#1164 - Número perfeito
N = int(input())
for i in range(0,N):
    X = int(input())

    soma = 0

    for divisor in range(1,X-1):
        if X % divisor == 0:
            soma += divisor

    if X == soma:
        print("%d eh perfeito" %(X))
    else: 
        print("%d nao eh perfeito" %(X))
