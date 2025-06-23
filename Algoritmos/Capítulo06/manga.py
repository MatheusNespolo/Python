#Vendedor de manga

#Importando módulos
from collections import deque

grafo = {}

grafo['Matheus'] = ['Tom', 'Joao', 'Maria']
grafo['Tom'] = ['Matheus', 'Joao', 'Maria']
grafo['Joao'] = ['Matheus', 'Tom', 'Maria']
grafo['Maria'] = ['Matheus', 'Tom', 'Joao']
grafo['Antonio'] = []
grafo['Roberto'] = []
grafo['Alfredo'] = []

fila_de_pesquisa = deque()
fila_de_pesquisa += grafo['Matheus']

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

while fila_de_pesquisa:
    pessoa = fila_de_pesquisa.popleft()
    if pessoa_e_vendedor(pessoa):
        print(pessoa, 'é um vendedor de manga.')
        break
    else:
        fila_de_pesquisa += grafo[pessoa]
        print('Não há um vendedor de manda')
        break
