sair = bool = False
cadastro = maiores = homens = mulheres = 0
while not sair:
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        maiores += 1
    sexo = str(input('Selecione o sexo - (M/F): '))
    if sexo in 'Mm':
        homens +=1
    elif sexo in 'Ff':
        if idade < 20:
            mulheres += 1
    else:
        sair == True
    cadastro += 1
    cont = str(input('Continuar? (S/N) '))
    if cont in 'Nn':
        sair == True
        break
    elif cont in 'Ss':
        sair == False
    else:
        sair == True
print(f'a) {maiores} maior(es) de idade\nb) {homens} homem(ns) e\nc) {mulheres} mulher(es) com menos de 20 anos.')