#Frequência na Aula
#https://neps.academy/br/exercise/252

numeros_unicos = set()  # Usamos um conjunto para armazenar os números únicos
N = int(input())
for _ in range(N):
    numero = int(input())
    numeros_unicos.add(numero)  # Adicionamos o número ao conjunto

print(len(numeros_unicos))  # Imprimimos a quantidade de números únicos
