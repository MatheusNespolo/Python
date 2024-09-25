#Valores Entre Dois Números
A = int(input())
B = int(input())
lista = []
if B > A:
    for i in range(A, B + 1):
        lista.append(i)
elif A > B:
    for i in range(B, A + 1):
        lista.append(i)
print(" ".join(map(str, lista)))