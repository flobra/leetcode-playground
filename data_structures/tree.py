from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        if not self:
            return ""

        # Initialize queue for BFS
        queue = deque([self])
        result = []

        # Traverse the tree in BFS order
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")  # Placeholder for missing nodes

        # Join the result as a string, ignoring trailing "null" placeholders
        while result and result[-1] == "null":
            result.pop()

        return " -> ".join(result)

def list_to_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        # Process left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        # Process right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

# Helper function for level-order traversal
def print_tree_level_order(self, root: Optional[TreeNode]) -> List[Optional[int]]:
	if not root:
		return []

	result = []
	queue = deque([root])

	while queue:
		node = queue.popleft()
		if node:
			result.append(node.val)
			queue.append(node.left)
			queue.append(node.right)
		else:
			result.append(None)

	# Remove trailing None values for a cleaner output
	while result and result[-1] is None:
		result.pop()

	return result

# Helper function to see whether two trees are equal
def trees_are_equal(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2 or tree1.val != tree2.val:
        return False
    return trees_are_equal(tree1.left, tree2.left) and trees_are_equal(tree1.right, tree2.right)
