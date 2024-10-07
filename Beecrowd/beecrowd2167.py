#2167 - Falha no motor
def encontrar_queda(rpms):
    anterior = rpms[0]
    for i, rpm in enumerate(rpms[1:]):
        if rpm < anterior:
            return i+1
        anterior = rpm
    return -1

N = int(input())

rpms = [int(x) for x in input().split()]

indice = encontrar_queda(rpms)
if indice != -1:
    print(indice+1)
else:
    print(0)
