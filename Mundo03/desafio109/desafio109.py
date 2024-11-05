import moeda2

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda2.moeda(p)} é {moeda2.metade(p, True)}')
print(f'O dobro de {moeda2.moeda(p)} é {moeda2.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda2.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda2.diminuir(p , 13, True)}')
