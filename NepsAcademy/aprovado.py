#Reprovado, Aprovado ou Final
N1 = float(input())
N2 = float(input())
media = (N1 * 2 + N2 * 3) / 5
if media >= 7:
    print('Aprovado')
elif media < 3:
    print('Reprovado')
else:
    print('Final')