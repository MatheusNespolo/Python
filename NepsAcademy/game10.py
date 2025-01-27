#Game-10

N = int(input())
D = int(input())
A = int(input())
res = 0

for i in range(N):
    if D > A:
        res = (D - A)
    elif D < A:
        res = (N - (A - D))

print(res)
