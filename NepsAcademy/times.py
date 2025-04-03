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

for k in range(N):
    if k % T == 0:
        #Adicionando o aluno ao time
        times[k % T].append(list(alunos.keys())[k])
    else:
        #Adicionando o aluno ao time
        times[k % T].append(list(alunos.keys())[k])

times_ordenados = {chave: sorted(nomes) for chave, nomes in times.items()}
#Ordenando os nomes dos alunos em ordem alfabética em outro dicionário

#Saída
for l in range(T):
    print(f'Time {l + 1}')
    for m in times_ordenados[l]:
        print(m)
    print()
#Imprimindo os times e os alunos
