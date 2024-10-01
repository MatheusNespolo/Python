#Fita Colorida
def proximo_pintado(valores):
    if not valores:
        return 0

    for i in range(0, len(valores)):
        if i == 0:
            if valores[i] == -1:
                index = valores.index(0)
                saida.append(index)
        elif i == 1:
            if valores[i] == valores[i-1]:
                saida.append(index-i)
        elif i == 2:
            if valores[i] == 0:
                saida.append(0)
        elif i > 2 and i < (len(valores)/2):
            if valores[i] == -1:
                index = valores[:i].index(0)
                saida.append(i-index)
            else:
                saida.append(0)
        else:
            index = valores[i:].index(0)
            saida.append(i-index)

    return saida

saida = []
N = int(input())
valores = list(map(int, input().split()))
colorida = proximo_pintado(valores)
print(colorida)    