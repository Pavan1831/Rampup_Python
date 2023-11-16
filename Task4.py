import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root):
    if not root:
        return []

    # Initialize a queue for BFS, where each item is a tuple (node, row, col)
    queue = collections.deque([(root, 0, 0)])
    # Create a dictionary to group nodes by column
    column_dict = collections.defaultdict(list)

    while queue:
        # Process nodes level by level
        level_dict = collections.defaultdict(list)
        for _ in range(len(queue)):
            node, row, col = queue.popleft()
            level_dict[col].append(node.val)

            if node.left:
                queue.append((node.left, row + 1, col - 1))
            if node.right:
                queue.append((node.right, row + 1, col + 1))

        # Merge the level's data into the column dictionary
        for col, nodes in level_dict.items():
            column_dict[col].extend(sorted(nodes))

    # Sort the columns based on their keys (column values)
    sorted_columns = sorted(column_dict.items())

    # Extract the sorted node values
    result = [[val for val in nodes] for col, nodes in sorted_columns]

    return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

result = verticalTraversal(root)

print(result)
