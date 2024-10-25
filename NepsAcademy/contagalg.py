#Contagem de Algarismos
N = int(input())
lista = []
contagens = []
algarismos = [0,1,2,3,4,5,6,7,8,9]

for i in range(N):
    num = int(input())
    lista.append(num)

for algarismo in algarismos:
    contagem = lista.count(algarismo)
    contagens.append(contagem)

for j in range(len(algarismos)):
    print(f'{j} - ',f'{contagens[j]}')  # Output: [3, x, x, x, x, x, x, x, x]
