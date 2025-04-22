#Dividir para conquistar
#Página 77

# Neps
# #Soma dos Elementos
# N = int(input())
# valores = list(map(int, input().split()))
# print(sum(valores))

#Guia ilustrado
def soma(lista):
    resultado = 0
    if len(lista) < 2:
        return lista
    else:
        for i in lista:
            resultado += i
        return resultado

print(soma(lista=[2, 4, 6]))
