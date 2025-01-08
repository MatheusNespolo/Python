# lst = [3,4,6]
# print(lst[2])

# Tratamento de erros e exceções

# try:
#     a = int(input('Numerador: '))
#     b = int(input('Denominador: '))
#     r = a / b
# except Exception as erro:
#     print(f'Problema encontrado: {erro.__class__}.')
# else:
#     print(f'O resultado é {r:.1f}')
# finally:
#     print('Volte sempre. Muito obrigado!')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Houve um problema com o tipo dos dados inseridos.')
except ZeroDivisionError:
    print('O programa não aceita divisões por zero.')
except KeyboardInterrupt:
    print('O usuário escolheu sair do programa.')
except Exception as erro:
    print(f'O erro encontrado foi: {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre. Muito obrigado!')
