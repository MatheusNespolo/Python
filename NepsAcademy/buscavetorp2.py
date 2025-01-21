#Busca Simples no Vetor 03

v = list(map(int, input().split())) # Cria e mapeia o vetor como uma lista "v"
X = int(input())                    # Indica qual valor será buscado no vetor
ind = []
vezes = 0

for i in v:
    if i == X:
        vezes += 1
        ind.append(v.index(X))
        v[v.index(X)] = -1  # Substitui o valor encontrado por -1 para não ser contado novamente

if ind == []:   # Se a lista estiver vazia, significa que o valor não foi encontrado
    print('Mia x')
else:          # Caso contrário, imprime a quantidade de vezes que o valor foi encontrado e as posições
    print(vezes)
    for f in ind:
        print(f, end=' ')
