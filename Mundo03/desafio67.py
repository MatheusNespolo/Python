num = 0
while True:
    num = int(input('Selecione um valor de 1 a 9: '))
    if num < 0:
        break
    for i in range(1,11):
        print(f'{i} x {num} = {num*i}')
        i += 1