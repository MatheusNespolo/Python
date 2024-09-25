#Campo minado
N = int(input())
tabuleiro = []
for _ in range(N):
    tabuleiro.append(int(input()))
# Função para contar o número de minas em torno de cada célula
def campo_minado(tabuleiro):
    N = len(tabuleiro)
    resultado = [0] * N

    for i in range(N):
        minas = tabuleiro[i]
        if i > 0:
            minas += tabuleiro[i - 1]
        if i < N - 1:
            minas += tabuleiro[i + 1]
        resultado[i] = minas
    return resultado

resultado = campo_minado(tabuleiro)
for res in resultado:
    print(res)
