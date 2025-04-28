#Álbum da Copa
#https://neps.academy/br/exercise/163

N = int(input())
M = int(input())
compradas = set()

for _ in range(M):
    X = int(input())
    compradas.add(X)
    
print(N - len(compradas))
