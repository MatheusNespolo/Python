# Torres de Hanói

discos = []

while True:
    N = int(input())
    if N == 0:
        break
    discos.append(N)

for i in range(len(discos)):
    print(f'Teste {i + 1}')
    print(2 ** discos[i] - 1)
    print()
