#Tuplas são imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata frita')
for comida in lanche:
    print(comida)
for cont in range(0, len(lanche)):
    print(lanche[cont])
    cont += 1
for pos, comida in enumerate(lanche):
    print(pos, comida)

print(sorted(lanche))

pessoa = ('Matheus', 22, 'M', 73.4)
print(pessoa)