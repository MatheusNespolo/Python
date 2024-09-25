#Ordenação simples
N = int(input())
numeros = []
entrada = input()
numeros = list(map(int, entrada.split()))
ordem = sorted(numeros)
print(" ".join(map(str, ordem)))