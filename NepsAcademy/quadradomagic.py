#Quadrado Mágico (OBI 2007)
def verificar_quadrado_magico(matriz):

  n = len(matriz)
  soma_magica = sum(matriz[0])

  for linha in matriz:
    if sum(linha) != soma_magica:
      return -1

  for j in range(n):
    soma_coluna = sum(matriz[i][j] for i in range(n))
    if soma_coluna != soma_magica:
      return -1

  soma_diagonal_principal = sum(matriz[i][i] for i in range(n))
  soma_diagonal_secundaria = sum(matriz[i][n - 1 - i] for i in range(n))
  if soma_diagonal_principal != soma_magica or soma_diagonal_secundaria != soma_magica:
    return -1

  return soma_magica

N = int(input())
linhas = []
for _ in range(N):
  linha = list(map(int, input().split()))
  linhas.append(linha)

soma_magica = verificar_quadrado_magico(linhas)
if soma_magica != -1:
  print(soma_magica)
else:
  print(-1)