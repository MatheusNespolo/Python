# Olimpíadas

# Recebendo a entrada
N, M = map(int, input().split())

# N = número de países, M = número de modalidades

# Inicializando a lista de países e medalhas
paises = list(range(1, N + 1))  # Países são numerados de 1 a N
medalhas = {'ouro': [0] * N, 'prata': [0] * N, 'bronze': [0] * N}  # Dicionário para contar medalhas

# Lendo as medalhas de cada modalidade
for _ in range(M):
    O, P, B = map(int, input().split())
    medalhas['ouro'][O - 1] += 1  # Subtraímos 1 porque os países começam em 1
    medalhas['prata'][P - 1] += 1
    medalhas['bronze'][B - 1] += 1

# Criando uma lista de tuplas para ordenação
classificacao = []
for i in range(N):
    classificacao.append((medalhas['ouro'][i], medalhas['prata'][i], medalhas['bronze'][i], paises[i]))

# Ordenando a classificação
# Ordenamos primeiro pelo ouro, depois prata, depois bronze, e finalmente pelo número do país
classificacao.sort(reverse=True, key=lambda x: (x[0], x[1], x[2], -x[3]))

# Extraindo a ordem dos países
ordem_paises = [pais for (_, _, _, pais) in classificacao]

# Exibindo a classificação final em uma única linha
print(" ".join(map(str, ordem_paises)))
