#Evitando entradas duplicadas
#Página 100

votaram = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
        print('Mande embora!')
    else:
        votaram[nome] = True
        print('Deixe votar')

verifica_eleitor('Matheus')
verifica_eleitor('Tom')
verifica_eleitor('Tom')
