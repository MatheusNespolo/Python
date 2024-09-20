import tabulate
custos = (
    ('Lápis', 1.75),
    ('Borracha', 2.00),
    ('Caderno', 15.9),
    ('Estojo', 25.00)
)
print('-'*30)
print('LISTAGEM DE PREÇOS')
print('-'*30)
def listar_produtos_tabular():

    tabela = tabulate.tabulate(custos, headers = ['Produto', 'Preço (R$)', tablefmt:='grid'])
    print(tabela)

listar_produtos_tabular()