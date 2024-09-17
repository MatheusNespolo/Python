# Triângulo retângulo
import math
cato = float(input('Informe o valor do cateto oposto : '))
cata = float(input('Informe o valor do cateto adjacente: '))
hip = math.hypot(cato, cata)
print('A hipotenusa do triângulo retângulo cujo os catetos são {} e {} é {}'.format(cato,cata,hip))