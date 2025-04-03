#Expressões
#https://neps.academy/br/exercise/271


#Entrada
instancias = []
#Lista de strings para armazenar as instâncias
T = int(input())
#Número de instâncias

for i in range(T):
    A = str((input()))
    instancias.append(A)
#Adiciona o conjunto de caracteres como itens (strings) da lista

#Processamento
respostas = []
#Lista de respostas para armazenar os resultados
for j in range(T):
    if instancias[j].find(')') < instancias[j].find('(') or instancias[j].find(']') < instancias[j].find('[') or instancias[j].find('}') < instancias[j].find('{'):
        respostas.append('N')
    else:
        if instancias[j].count('(') == instancias[j].count(')'):
            if instancias[j].count('{') == instancias[j].count('}'):
                if instancias[j].count('[') == instancias[j].count(']'):
                    respostas.append('S')
                else:
                    respostas.append('N')
            else:
                respostas.append('N')
        else:
            respostas.append('N')
#Verifica se o número de caracteres de cada tipo é igual, se sim, adiciona 'S' à lista de respostas, caso contrário, adiciona 'N'.

#Saída
for k in respostas:
    print(k)
#Imprime as respostas