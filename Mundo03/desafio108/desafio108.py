import moeda1

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda1.moeda(p)} é {moeda1.moeda(moeda1.metade(p))}')
print(f'O dobro de {moeda1.moeda(p)} é {moeda1.moeda(moeda1.dobro(p))}')
print(f'Aumentando 10%, temos {moeda1.moeda(moeda1.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda1.moeda(moeda1.diminuir(p , 13))}')
