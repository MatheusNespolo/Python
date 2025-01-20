#Fuga

H, P, F, D = list(map(int, input().split()))

if D == 1:  # anti-horário
    pos_f = F
    while True:
        pos_f = (pos_f + 1) % 16
        if pos_f == H:
            print('S')
            break
        elif pos_f == P:
            print('N')
            break
else:   # horário
    pos_f = F
    while True:
        pos_f = (pos_f - 1 + 16) % 16
        if pos_f == H:
            print('S')
            break
        elif pos_f == P:
            print('N')

#  Não atualiza as posições do fugitivo

# if H < P and P < F or H > P and P < F:
#     if D == 1:
#         print('S')
#     else:
#         print('N')
# elif H < P and P > F or H > P and P > F:
#     if D == -1:
#         print('S')
#     else:
#         print('N')
