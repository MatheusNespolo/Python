#Máquina de Café
#https://neps.academy/br/exercise/95

#Entrada
A1 = int(input())
A2 = int(input())
A3 = int(input())
FuncionariosPorAndar = [A1, A2, A3]

#Processamento e Saída
AndarDaMaquina = FuncionariosPorAndar.index(max(FuncionariosPorAndar))

if AndarDaMaquina == 0:
    print(A2 * 2 + A3 * 4)
if AndarDaMaquina == 1:
    print(A1 * 2 + A3 * 2)
if AndarDaMaquina == 2:
    print(A1 * 4 + A2 * 2)
