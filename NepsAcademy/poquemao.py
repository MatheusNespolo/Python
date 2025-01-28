#Po que mão

N = int(input())
X = int(input())
Y = int(input())
Z = int(input())
poquemaos = 0

if (N - X) >= 0:
    poquemaos += 1
    N -= X
if (N - Y) >= 0:
    poquemaos += 1
    N -= Y
if (N - Z) >= 0:
    poquemaos += 1
    N -= Z

print(poquemaos)

# Não finalizado