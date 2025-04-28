#Lâmpadas do Hotel
#https://neps.academy/br/exercise/59

Ia, Ib, Fa, Fb = map(int, input().split())

if (Ia, Ib) == (Fa, Fb):
    print(0)
elif (1 - Ia, Ib) == (Fa, Fb):
    print(1)
elif (1 - Ia, 1 - Ib) == (Fa, Fb):
    print(1)
else:
    print(2)
