#Huaauhahhuahau

risada = str(input())
consoantes = 'bcdfghjkhlmnpqrstvwxyz'
for i in range(0,len(consoantes)):
    risada = risada.replace(consoantes[i],'')

risadaInvertida = risada[::-1]

if risada == risadaInvertida:
    print('S')
else:
    print('N')
