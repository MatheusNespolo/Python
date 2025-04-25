#Máquina de Café
#https://neps.academy/br/exercise/95

#Entrada
A1 = int(input())
A2 = int(input())
A3 = int(input())
FuncionariosPorAndar = []
FuncionariosPorAndar.append(A1)
FuncionariosPorAndar.append(A2)
FuncionariosPorAndar.append(A3)

#Processamento
AndarDaMaquina = FuncionariosPorAndar.index(max(FuncionariosPorAndar))
FuncionariosPorAndar.remove(max(FuncionariosPorAndar))

if AndarDaMaquina == 0:
    MinutosTomados = FuncionariosPorAndar[0] * 2 + FuncionariosPorAndar[1] * 4
if AndarDaMaquina == 1:
    MinutosTomados = FuncionariosPorAndar[0] * 2 + FuncionariosPorAndar[1] * 2
if AndarDaMaquina == 2:
    MinutosTomados = FuncionariosPorAndar[0] * 4 + FuncionariosPorAndar[1] * 2

#Saída
print(MinutosTomados)
