num = int(input('Digite um número inteiro: '))
primo = bool
for c in range (2,num-1):
    if num%c==0:
        primo = 0
    elif num%c!=0:
        primo = 1
if primo:
    print('{} é um número primo.'.format(num))
else:
    print('{} não é um número primo.'.format(num))