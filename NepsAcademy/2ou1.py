#Zerinho ou um
A, B, C = map(int, input().split())
if A == 1 and B == 0 and C == 0:
    print('A')
elif A == 0 and B == 1 and C == 1:
    print('A')
if A == 0 and B == 1 and C == 0:
    print('B')
elif A == 1 and B == 0 and C == 1:
    print('B')
if A == 0 and B == 0 and C == 1:
    print('C')
elif A == 1 and B == 1 and C == 0:
    print('C')
if A == 0 and B == 0 and C == 0:
    print('*')
elif A == 1 and B == 1 and C == 1:
    print('*')
