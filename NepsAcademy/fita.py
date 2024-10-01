#Fita Colorida
def calcular_distancia(fita):
  distancias = []
  for i in range(len(fita)):
    if fita[i] == -1:
      menor_distancia = float('inf')
      for j in range(len(fita)):
        if fita[j] == 0:
          distancia = abs(i - j)
          menor_distancia = min(menor_distancia, distancia)
      if menor_distancia > 9:
        menor_distancia = 9
      distancias.append(menor_distancia)
    else:
      distancias.append(fita[i])
  return distancias

N = int(input())
fita = list(map(int, input().split()))
distancias = calcular_distancia(fita)

print(*distancias)