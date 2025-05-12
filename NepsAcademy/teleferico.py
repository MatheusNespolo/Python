#Teleférico
#https://neps.academy/br/exercise/15

# Versão matemática + condicional (apresentou erro)
# C = int(input())
# A = int(input())
# viagens = 0

# if C >= (A + 1):
#     viagens = 1
# elif C < (A + 1):
#     viagens = ((A + 1) // C)

# print(viagens)

# Versão recursiva (apresentou erro)
# C = int(input())
# A = int(input())
# viagens = 0

# if A <= (C - 1):
#     viagens = 1
# else:
#     while A > 0:
#         A = A - (C - 1)
#         viagens += 1

# print(viagens)

# Versão matemática
C = int(input())
A = int(input())

capacidade = C - 1
viagens = (A + capacidade - 1) // capacidade

print(viagens)
