#Cobra Coral

p = list(map(int, input().split())) # Cria e mapeia o vetor como uma lista "p"

for i in range(len(p)): # Percorre o vetor
    p.count(p[i]) # Conta quantas vezes o valor p[i] aparece no vetor
    if p.count(p[i]) > 1: # Se o valor aparecer mais de uma vez
        dife = (p.index(p[i])) - (p.index(p[i])+1) # Subtrai a posição do primeiro valor encontrado pela posição do segundo valor encontrado
    if dife > 1:
        print('F')
        break
    else:
        print('V')
        break
