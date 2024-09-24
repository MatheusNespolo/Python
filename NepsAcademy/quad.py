#Quadrante
X = int(input())
Y = int(input())
if X > 0 and Y > 0:
    print('Q1')
elif X < 0 and Y > 0:
    print('Q2')
elif X < 0 and Y < 0:
    print('Q3')
elif X > 0 and Y < 0:
    print('Q4')
elif X == 0 or Y == 0:
    print('eixos')