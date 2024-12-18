#Huaauhahhuahau

risada = str(input())
consoantes = 'bcdfghjkhlmnpqrstvwxyz'
for i in range(0,len(consoantes)):
    risada = risada.replace(consoantes[i],'')

print(risada)
