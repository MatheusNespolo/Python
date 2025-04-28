#Teleférico
#https://neps.academy/br/exercise/15

C = int(input())
A = int(input())
viagens = 0

if C >= (A + 1):
    viagens = 1
elif C < (A + 1):
    viagens = ((A + 1) // C)

print(viagens)
