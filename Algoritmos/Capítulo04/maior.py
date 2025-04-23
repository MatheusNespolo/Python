#Maior valor de uma lista
#Página 77

def maior(lista):
    maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

print(maior([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
