#  Fatias limitadas

from collections import deque

def solution(K, A):
    N = len(A)
    esquerda = 0
    contador = 0
    min_deque = deque()
    max_deque = deque()
    
    for direita in range(N):
        # Atualiza o min_deque
        while min_deque and A[direita] < A[min_deque[-1]]:
            min_deque.pop()
        min_deque.append(direita)
        
        # Atualiza o max_deque
        while max_deque and A[direita] > A[max_deque[-1]]:
            max_deque.pop()
        max_deque.append(direita)
        
        # Não atende = incremento 'esquerda'
        while A[max_deque[0]] - A[min_deque[0]] > K:
            esquerda += 1
            if min_deque[0] < esquerda:
                min_deque.popleft()
            if max_deque[0] < esquerda:
                max_deque.popleft()
        
        # conta o número de fatias válidas que iniciam na 'direita'
        contador += direita - esquerda + 1
        
        # Execeção 1,000,000,000
        if contador > 1_000_000_000:
            return 1_000_000_000
    
    return contador

