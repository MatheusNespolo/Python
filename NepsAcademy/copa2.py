def determinar_campeao(resultados):
    # Definição das chaves de acordo com a imagem
    chaves = [
        ('A', 'B'), ('C', 'D'), ('E', 'F'), ('G', 'H'),
        ('I', 'J'), ('K', 'L'), ('M', 'N'), ('O', 'P')
    ]
    
    quartas = []
    for i in range(8):
        m, n = resultados[i]
        vencedor = chaves[i][0] if m > n else chaves[i][1]
        quartas.append(vencedor)
    
    semi = []
    for i in range(4):
        m, n = resultados[8 + i]
        vencedor = quartas[2 * i] if m > n else quartas[2 * i + 1]
        semi.append(vencedor)
    
    finalistas = []
    for i in range(2):
        m, n = resultados[12 + i]
        vencedor = semi[2 * i] if m > n else semi[2 * i + 1]
        finalistas.append(vencedor)
    
    # Jogo final
    m, n = resultados[14]
    campeao = finalistas[0] if m > n else finalistas[1]
    
    print(campeao)

# Leitura da entrada
dados = []
for _ in range(15):
    m, n = map(int, input().split())
    dados.append((m, n))

determinar_campeao(dados)
