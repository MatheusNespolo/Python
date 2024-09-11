peso = ['','','','','']
for c in range (0,5):
    peso[c] = float(input('Digite o peso da pessoa {} (Kg): '.format(c+1)))
print('O maior peso lido foi: {}Kg'.format(max(peso)))
print('O menor peso lido foi: {}Kg'.format(min(peso)))
