#Móbile (OBI 2015)

A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A == (B + C + D) and D == (B + C) and B == C:
    print('S')
else:
    print('N')
