#Expressões
#https://neps.academy/br/exercise/271
# Entrada
T = int(input())
instancias = [input() for _ in range(T)]

# Função para validar expressões com pilha
def verifica_expressao(expr):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expr:
        if char in "({[":
            pilha.append(char)
        elif char in ")}]":
            # Se a pilha está vazia ou o topo da pilha não corresponde ao caractere atual
            if not pilha or pilha[-1] != pares[char]:
                return "N"
            pilha.pop()  # Remove o par correspondente

    # Se a pilha ainda tiver elementos, há parênteses não fechados corretamente
    return "S" if not pilha else "N"

# Processamento e saída
for instancia in instancias:
    print(verifica_expressao(instancia))