#Troco em Moedas
#https://neps.academy/br/exercise/143

C = int(input())

moedas = [100, 50, 25, 10, 5, 1]
quantMoedas = []

totalMoedas = 0

if C == 0:
    print(0)*7
elif C > 0:
    for moeda in moedas:
        totalMoedas += C//moeda
        quantMoedas.append(int(C/moeda))
        C = C % moeda
print(totalMoedas)
for moeda in quantMoedas:
    print(moeda)
