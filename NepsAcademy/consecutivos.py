#Consecutivos
def calcular_pontos(valores):
  if not valores:
    return 0

  sequencia_atual = 1
  maior_sequencia = 1

  for i in range(1, len(valores)):
    if valores[i] == valores[i - 1]:
      sequencia_atual += 1
    else:
      sequencia_atual = 1

    maior_sequencia = max(maior_sequencia, sequencia_atual)

  return maior_sequencia

N = int(input())
valores = list(map(int, input().split()))
pontos = calcular_pontos(valores)
print(pontos)