#Dez Valores

X = int(input())
proximos = []
final = ''

for i in range(1, 11):
    proximos.append(X+i)

for itens in proximos:
    final += str(itens) + ' '

print(final)
