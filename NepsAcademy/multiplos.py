#Múltiplos de 2, 3 e 4

N = int(input())

multiplosDe2 = 0
multiplosDe3 = 0
multiplosDe4 = 0

for i in range(1, N + 1):
    num = int(input())
    if num % 2 == 0:
        multiplosDe2 += 1
    if num % 3 == 0:
        multiplosDe3 += 1
    if num % 4 == 0:
        multiplosDe4 += 1

print(f'{multiplosDe2}')
print(f'{multiplosDe3}')
print(f'{multiplosDe4}')
