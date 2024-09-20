#Lâmpadas
A = 0
B = 0

def I1():           # Função para simular o interruptor I1
  global A
  A = 1 - A

def I2():           # Função para simular o interruptor I2
  global A, B
  A = 1 - A
  B = 1 - B

N = int(input())
sequencia = list(map(int, input().split()))

def pressionados(seq):     # Função para simular a sequência de interruptores
  for interruptor in seq:
    if interruptor == 1:
      I1()
    elif interruptor == 2:
      I2()

pressionados(sequencia)
print(A)
print(B)
