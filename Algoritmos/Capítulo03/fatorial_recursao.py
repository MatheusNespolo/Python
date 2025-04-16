#A pilha de chamada com recursão
#Página 64

def fat(x):
    if x==1:
        return 1
    else:
        return x * fat(x-1)
    
print(fat(3))
