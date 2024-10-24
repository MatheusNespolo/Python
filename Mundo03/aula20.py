def mostraLinha():
    print('-='*30)


mostraLinha()
print('         SISTEMA DE ALUNOS')
mostraLinha()
print('         CADASTRO DE FUNCIONÁRIOS')
mostraLinha()
print('         ERRO DO SISTEMA')

def mensagem(msg):
    mostraLinha()
    print(msg)
    mostraLinha()

mensagem('Mensagem padrão')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A e B é igual a {s}.')

#Soma com função
soma(3, 5)

def contador(*num):
    tam = len(num)
    print(f'Foram recebidos {tam} números.')

contador(2, 1, 7)
contador(8, 9)
contador(4, 3, 6, 5)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [7, 2, 5, 0, 4]
dobra(valores)
print(valores)

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')

soma(7, 2, 5, 0, 4)