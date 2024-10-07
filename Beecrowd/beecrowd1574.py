#1574 - Instruções do Robô
def posicao_robo(passos):
  posicao = 0
  feito = []
  for i, instru in enumerate(passos):
    if instru == "LEFT":
      posicao -= 1
      feito.append("LEFT")
    elif instru == "RIGHT":
      posicao += 1
      feito.append("RIGHT")
    elif instru.startswith("SAME AS"):
      j = int(instru.split()[-1]) - 1
      refazer = feito[j]
      if refazer == "LEFT":
        posicao -= 1
      elif refazer == "RIGHT":
        posicao += 1
      feito.append(refazer)
  return posicao

T = int(input())
for _ in range(T):
  N = int(input())
  passos = [input() for _ in range(N)]
  final = posicao_robo(passos)
  print(final)
