#Chaves
#https://neps.academy/br/exercise/56

def confere_chaves():
    #Entrada
    linhas = int(input())
    codigo = str()
    validacao = False

    #Processamento
    for _ in range(linhas):
        linha_do_codigo = str(input())
        codigo += linha_do_codigo

    if '{' not in codigo and '}' not in codigo:
        validacao = True
    if codigo.count('{') == codigo.count('}'):
        validacao = True
    else:
        validacao = False
        
    #Saída
    if validacao:
        print('S')
    else:
        print('N')

#Chamda da função
confere_chaves()
