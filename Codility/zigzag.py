from dataclasses import dataclass

# Define the Tree class
@dataclass
class Tree:
    x: int = 0
    l: "Tree" = None
    r: "Tree" = None

# Solution function to find the longest zigzag path
def solution(T):
    max_length = 0

    def dfs(node, direction, length):
        nonlocal max_length
        if not node:
            return
        
        # Update the maximum length found so far
        max_length = max(max_length, length)
        
        # If the previous direction was left, go right, and vice versa
        if direction == 'left':
            dfs(node.r, 'right', length + 1)
            dfs(node.l, 'left', 1)  # Reset if continuing in the same direction
        else:
            dfs(node.l, 'left', length + 1)
            dfs(node.r, 'right', 1)  # Reset if continuing in the same direction
    
    # Start by going left and right from the root
    if T:
        dfs(T.l, 'left', 1)
        dfs(T.r, 'right', 1)

    return max_length

# Test Cases

# Example Tree from the Image
T = Tree(5,
         Tree(3,
              Tree(20,
                   Tree(6, None, None),
                   None),
              None),
         Tree(10,
              Tree(1, None, None),
              Tree(15,
                   Tree(30,
                        None,
                        Tree(9, None, None)),
                   Tree(8, None, None))))

print(solution(T))  # Expected output: 2

# Test Case: Single Node
T = Tree(1)
print(solution(T))  # Expected output: 0

# Test Case: Straight Zigzag Tree
T = Tree(1,
         Tree(2,
              None,
              Tree(3,
                   Tree(4, None, None),
                   None)),
         None)
print(solution(T))  # Expected output: 3

# Test Case: Empty Tree
print(solution(None))  # Expected output: 0

# Test Case: Tree with no zigzag (only left children)
T = Tree(1, Tree(2, Tree(3, None, None), None), None)
print(solution(T))  # Expected output: 0
