def resumo(n, aum, red):
    print('-'*40)
    print(f'    RESUMO DO VALOR')
    print('-'*40)
    print(f'Preço analisado:    R${n:.0f},00')
    print(f'Dobro do preço:     R${2*n:.0f},00')
    print(f'Metade do preço:    R${n/2:.0f},00')
    print(f'80% de aumento:     R${n + (n*(aum/100)):.0f},00')
    print(f'30% de redução:     R${n - (n*(red/100)):.0f},00')