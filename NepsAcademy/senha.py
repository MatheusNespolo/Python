#Senha

senha = 2018
quanti = 0
chute = 0

while chute != senha:
    chute = int(input())
    quanti += 1
    if chute == senha:
        break
print(quanti-1)
