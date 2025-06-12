#Chaves
#https://neps.academy/br/exercise/56

def confere_chaves():
    #Entrada
    linhas = int(input())
    codigo = ''

    #Processamento
    for _ in range(linhas):
        linha_do_codigo = str(input())
        codigo += linha_do_codigo
    
    pilha = []
    validacao = True

    for char in codigo:
        if char == '{': # Se for uma abertura de chave adiciona ela a pilha
            pilha.append('{')
        elif char == '}': # Se o caractere for de fechamento
            if len(pilha) == 0: # Verifica se a pilha está vazia
                validacao = False # Se estiver: fechamento antes de abertura
                break
            else:
                pilha.pop() # Remove a abertura da chave da pilha
    
    if len(pilha) != 0: # Ao final da verificação a pilha deve estar vazia
        validacao = False
        
    #Saída
    if validacao:
        print('S')
    else:
        print('N')

#Chamda da função
confere_chaves()
