#Fita Colorida
saida = []
N = int(input())
valores = list(map(int, input().split()))
for i in range(1, len(valores)):
    if valores[i] == 0:
        saida.append(0)
    elif valores[i] < 0:
        saida.append(valores.index(0))