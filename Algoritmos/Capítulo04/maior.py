#Maior valor de uma lista
#Página 77

def maior(lista):
    maior = 0
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior

print(maior([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#Sugestão
def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max

print(maximo([1,2,3,4,5,6,7,8,9,10]))
