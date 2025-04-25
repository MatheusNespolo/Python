#Álbum da Copa
#https://neps.academy/br/exercise/163

N = int(input())
M = int(input())
compradas = []

for _ in range(M):
    X = int(input())
    compradas.append(X)

for figurinhas in compradas:
    while compradas.count(figurinhas) > 1:
        compradas.remove(figurinhas)
    
print(N - len(compradas))
