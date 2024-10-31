def notas(n, sit=True):
    """ Função para anlisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando ou não a situação.
    :return: dicionário com várias informações da turma.
    """
    if situ in 'Ss':
        sit = True
    else:
        sit = False
    dic['Total'] = len(n)
    dic['Maior'] = max(n)
    dic['Menor'] = min(n)
    dic['Média'] = (sum(n) / len(n))
    if sit == True:
        if dic['Média'] < 6:
            dic['Situação'] = 'RUIM'
        elif 6 <= dic['Média'] < 8:
            dic['Situação'] = 'RAZOÁVEL'
        elif 8 <= dic['Média'] < 10:
            dic['Situação'] = 'BOA'
    return dic

dic = {
    'Total':'',
    'Maior':'',
    'Menor':'',
    'Média':'',
}

lista = []
while True:
    lista.append(float(input('Digite as notas da sala: ')))
    esc = str(input('Deseja continuar? (S/N) '))
    if esc in 'Nn':
        break
situ = str(input('Deseja mostrar a situação? (S/N) '))

resp = notas(lista)
print(resp)