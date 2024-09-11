frase = input('Digite uma frase: ')
frase_inv = (frase[::-1])
if frase == frase_inv:
    print('{} invertido seria {}. A frase é um palíndromo.'.format(frase, frase_inv))
else:
    print('{} invertido seria {}. A frase não é um palíndromo.'.format(frase, frase_inv))