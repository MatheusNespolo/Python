#Times
#https://neps.academy/br/exercise/253

#Entrada
alunos = {}
N, T = map(int, input().split())
#Quantidade de alunos e número de times
for i in range(N):
    nome, nivel = input().split()
    #Nome e habilidade do aluno
    alunos[nome] = int(nivel)
    #Criando dicionário com os alunos e suas habilidades

#Processamento
alunos = dict(sorted(alunos.items(), key=lambda item: item[1], reverse=True))
#Ordenando os alunos por habilidade em ordem decrescente

times = {}
for j in range(T):
    times[i] = []
    #Criando dicionário para os times
    for k in range(i, N, T):
            times[i].append(list(alunos.keys())[j])
            #Adicionando os alunos aos times

#Saída
for i in range(T):
    print(f'Time {i+1}:', end=' ')
    for j in range(len(times[i])):
        print(times[i][j], end=' ')
    print()
#Imprimindo os times e os alunos
