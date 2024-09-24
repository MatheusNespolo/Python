#Vestibular
acerto = 0
m = 0
N = int(input())
gabarito = input()
resposta = input()
for m, letra in enumerate(gabarito):
    if letra == resposta[m]:
        acerto += 1
    m += 1
print(acerto)