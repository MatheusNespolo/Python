#Fibonacci
n = int(input())
n1, n2 = 0, 1
count = 0
while count < n:
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
print(n2)
