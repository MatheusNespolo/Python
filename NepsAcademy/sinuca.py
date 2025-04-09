#Tacos de Bilhar
#https://neps.academy/br/exercise/54


#Entrada
estoque = set()
produzidos = 0
C = int(input())
comprimentos = list(map(int, input().split()))

#Processamento
for comprimento in comprimentos:
    if comprimento in estoque:
        estoque.remove(comprimento)
    else:
        estoque.add(comprimento)
        produzidos += 2

#Saída
print(produzidos)
