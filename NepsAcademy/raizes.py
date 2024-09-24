#Raízes
import math
N = int(input())
X = input()
numeros = list(map(float, X.split()))
raizes = [math.sqrt(num) for num in numeros]
for raiz in (raizes):
    print(f'{raiz:.4f}')