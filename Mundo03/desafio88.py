#Mega sena
import random
cont = 0
jogo = []
print('-'*20)
print(' JOGO DA MEGA SENA')
print('-'*20)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0,jogos):
        def palpite():
            return random.sample(range(1,61), 6)
        gera_palpite = palpite()
        jogo.append(sorted(gera_palpite[:]))
        print(f'Jogo {i}: {jogo}')
        jogo.clear()
