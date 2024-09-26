valores = []
pares = []
impares = []
for i in range(0,7):
    valores.append(int(input('Digite um valor numérico: ')))
    if valores[i] % 2 == 0:
        pares.append(valores[i])
    else:
        impares.append(valores[i])
pareso = sorted(pares)
impareso = sorted(impares)
print(f'Os valores pares digitados foram: {pareso}')
print(f'Os valores ímpares digitados foram: {impareso}')
