#Cobra Coral

p = list(map(int, input().split())) # Cria e mapeia o vetor como uma lista "p"
res = ''

if res != 'F' and res != 'V': # Se a resposta não for F ou V
    for i in range(len(p)): # Percorre o vetor
        p.count(p[i]) # Conta quantas vezes o valor p[i] aparece no vetor
        if p.count(p[i]) == 2:
            vez1 = p.index(p[i])
            vez2 = p.index(p[i], vez1 + 1) # Procura a segunda ocorrência do valor p[i]
            if vez2 - vez1 == 2:
                res = 'V'
            else:
                res = 'F'

print(res)
