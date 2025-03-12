from collections import deque

def solution(K, A):
    N = len(A)
    left = 0
    count = 0
    min_deque = deque()
    max_deque = deque()
    
    for right in range(N):
        # Maintain min deque
        while min_deque and A[right] < A[min_deque[-1]]:
            min_deque.pop()
        min_deque.append(right)
        
        # Maintain max deque
        while max_deque and A[right] > A[max_deque[-1]]:
            max_deque.pop()
        max_deque.append(right)
        
        # If the current window is invalid, shrink it from the left
        while A[max_deque[0]] - A[min_deque[0]] > K:
            left += 1
            if min_deque[0] < left:
                min_deque.popleft()
            if max_deque[0] < left:
                max_deque.popleft()
        
        # Count the number of valid slices ending at 'right'
        count += right - left + 1
        
        # Early termination if count exceeds 1,000,000,000
        if count > 1_000_000_000:
            return 1_000_000_000
    
    return count
