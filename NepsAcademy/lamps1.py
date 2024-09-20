#Lâmpadas
A = 0
B = 0
N = int(input())
sequencia = list(map(int, input().split()))
for interruptor in sequencia:               # Sequência de interruptores
    if interruptor == 1:                    # Interruptor I1
        A = 1 - A
    if interruptor == 2:                    # Interruptor I2
        A = 1 - A
        B = 1 - B
print(A)
print(B)
