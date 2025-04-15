#Recursão
#Página 60

# def regressiva(i):
#     print(i)
#     regressiva(i-1)

# regressiva(10)
# #Erro de limite de recursão (sem caso-base)

#Recursão com caso-base

def regressiva(i):
    print(i)
    if i <= 1:  #Caso-base
        return
    else:       #Caso recursivo
        regressiva(i-1)

regressiva(10)
