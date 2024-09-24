#Medalhas
T1 = int(input())
T2 = int(input())
T3 = int(input())
lista = [T1, T2, T3]
if T1 < T2 and T1 < T3 and T2 < T3:
    print('1\n2\n3')
elif T1 < T2 and T1 < T3 and T3 < T2:
    print('1\n3\n2')
elif T2 < T1 and T2 < T3 and T1 < T3:
    print('2\n1\n3')
elif T2 < T1 and T2 < T3 and T3 < T1:
    print('2\n3\n1')
elif T3 < T1 and T3 < T2 and T1 < T2:
    print('3\n1\n2')
elif T3 < T1 and T3 < T2 and T2 < T1:
    print('3\n2\n1')
