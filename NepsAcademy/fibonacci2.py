#Sequência de Fibonacci
#https://neps.academy/br/exercise/173
sequencia = []
n = int(input())
n1, n2 = 0, 1
sequencia.append(n1)
sequencia.append(n2)
count = 0
while count < n:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    sequencia.append(n2)
    count += 1
for i in range(n):
    print(sequencia[i], end=' ')
