#Andando no Tempo
#https://neps.academy/br/exercise/111

A, B, C = map(int, input().split())

if A == B or A == C or B == C:
    print('S')
if A == (B + C) or B == (A + C) or C == (A + B):
    print('S')
else:
    print('N')
