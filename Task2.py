class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def postorderTraversal(root):
    if not root:
        return []

    result = []
    stack = [] # nodes to be visited
    current = root
    visited = set() # visited nodes

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            temp = stack[-1]
            if temp.right and temp not in visited:
                current = temp.right
                visited.add(temp)
            else:
                result.append(temp.val)
                stack.pop()

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(8)
result = postorderTraversal(root)
print(result)