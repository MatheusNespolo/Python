num1 = int(input('Digite o primeiro número inteiro: '))
num2 = int(input('Digite o segundo número inteiro: '))
if num1 > num2 or num2 < num1:
    print('O primeiro valor é maior que o segundo.')
elif num2 < num1 or num1 < num2:
    print('O segundo valor é maior que o primeiro.')
elif num1 == num2:
    print('Os valores são iguais.')