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
    times[j] = []
    #Criando dicionário para os times 

aluno = list(alunos.keys())
times[j].append(aluno)
alunos.popitem()
#Adicionando os alunos aos times, removendo da lista de alunos

#Saída

print(times)

#Imprimindo os times
