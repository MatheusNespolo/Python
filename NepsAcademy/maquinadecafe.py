#Máquina de Café
#https://neps.academy/br/exercise/95

#Entrada
A1 = int(input())
A2 = int(input())
A3 = int(input())

#Processamento e Saída
t1 = A2 * 2 + A3 * 4
t2 = A1 * 2 + A3 * 2
t3 = A1 * 4 + A2 * 2
if t1 <= t2 and t1 <= t3: print(t1)
elif t2 <= t1 and t2 <= t3: print(t2)
elif t3 <= t1 and t3 <= t2: print(t3)
