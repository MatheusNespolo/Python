#Prêmio do milhão
soma = 0
N = int(input())
for dias in range(0, N + 1):
    if soma >= 1000000:
        print(dias)
        break
    A = int(input())
    soma += A
    dias += 1
