#Chaves
#https://neps.academy/br/exercise/56

def confere_chaves():
    #Entrada
    N = int(input())
    codigo = []
    linhas_validadas = 0

    #Processamento
    for _ in range(N):
        linha_do_codigo = str(input())
        codigo.append(linha_do_codigo)

    for linha_do_codigo in codigo:
        chaves_abertas = 0
        chaves_fechadas = 0
        if '{' not in linha_do_codigo and '}' not in linha_do_codigo:
            linhas_validadas += 1
        if linha_do_codigo.count('{') > 0:
            chaves_abertas += linha_do_codigo.count('{')
        if linha_do_codigo.count('}') > 0:
            chaves_fechadas += linha_do_codigo.count('}')
        else:
            linhas_validadas = linhas_validadas
        
    #Saída
    if linhas_validadas == N:
        print('S')
    else:
        print('N')

#Chamda da função
confere_chaves()
