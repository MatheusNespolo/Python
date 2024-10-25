#Torre

N = int(input())

tabuleiro = []
somas_linhas = [0] * N
somas_colunas = [0] * N

for i in range(N):
  linha = list(map(int, input().split()))
  tabuleiro.append(linha)
  somas_linhas[i] = sum(linha)
  for j in range(N):
    somas_colunas[j] += linha[j]

peso_maximo = 0
for i in range(N):
  for j in range(N):
    peso = somas_linhas[i] + somas_colunas[j] - 2 * tabuleiro[i][j]
    peso_maximo = max(peso_maximo, peso)

print(peso_maximo)
