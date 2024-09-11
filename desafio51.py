print('-*'*20)
print('Progressão aritmética')
print('-*'*20)
prog = 0
termo = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão da progressão: '))
for c in range (termo, (termo + 11), raz):
    print(c)