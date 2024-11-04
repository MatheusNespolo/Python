#Busca Simples no Vetor 02

v = list(map(int, input().split())) # Cria e mapeia o vetor como uma lista "v"
X = int(input())                    # Indica qual valor será buscado no vetor
ind = []
vezes = 0

for i in v:
    if i == X:
        vezes += 1
        ind.append(v.index(X))
    
    else:
        break
print(vezes)
for f in ind:
    print(f, end=' ')
