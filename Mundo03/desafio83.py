exp = str(input('Escreva uma expressão entre parênteses: '))
if '(' in exp[0:-1]:
    if ')' in exp[1:]:
        print('Abertura e fechamento de parênteses corretos.')
else:
    print('Abertura e fechamento de parênteses incorretos.')