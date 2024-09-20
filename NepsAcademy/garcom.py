#Garçom
N = int(input())
quebrados = 0
for i in range(0,N):
    L, C = map(int, input().split())
    if L > C:
        quebrados += C
print(quebrados)
