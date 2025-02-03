#Botas Trocadas

N = int(input())
tamanhosD = []
tamanhosE = []
peD = 0
peE = 0

for i in range(N):
    tamanho, pe = map(str, input().split())
    if pe == 'D':
        peD += 1
        tamanhosD.append(int(tamanho))
    elif pe == 'E':
        peE += 1
        tamanhosE.append(int(tamanho))
    

if peD == peE and sum(tamanhosD) == sum(tamanhosE):
    print(int(N / peD))
