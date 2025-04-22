#Exercício 4.2
#Página 77

def itens_na_lista(lista):
    itens = 0
    if len(lista) < 1:
        return 0
    else:
        for i in range(len(lista)):
            if lista[i] != None:
                itens += 1
        return itens

print(itens_na_lista([1, 2, 3, 4, 5]))
