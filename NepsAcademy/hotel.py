#Lâmpadas do Hotel
#https://neps.academy/br/exercise/59

Ia, Ib, Fa, Fb = map(int, input().split())
contador = 0
C1 = bool = False
C2 = bool = False

if C1:
    Ia = 1 - Ia
if C2:
    Ia = 1 - Ia
    Ib = 1 - Ib

if Ia != Fa and Ib != Fb:
    C2 = True
    contador += 1
if Ia != Fa and Ib == Fb:
    C1 = True
    contador += 1
if Fa != Fb:
    C1 = True
    C2 = True
    contador += 2

print(contador)
