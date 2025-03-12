# A non-empty array A consisting of N integers is given

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    contador = 0;
    indice = 0;
    indicador = False;
    while not indicador:
        contador += 1
        indice = A[indice]
        if contador > len(A):
            indicador = True
            return contador
        if contador == len(A):
            return 1
        if indice == -1:
            return contador
    pass
