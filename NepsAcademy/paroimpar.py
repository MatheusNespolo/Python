#Jogo de Par ou Impar

P = int(input())
D1 = int(input())
D2 = int(input())

if (D1 + D2) % 2 == 0 and P == 0 or (D1 + D2) % 2 != 0 and P == 1:
    print(0)
elif (D1 + D2) % 2 == 0 and P == 1 or (D1 + D2) % 2 != 0 and P == 0:
    print(1)
