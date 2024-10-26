# /leetcode_problems/problem_951.py
# Solution for Leetcode Problem #951: Flip Equivalent Binary Trees
#
# https://leetcode.com/problems/flip-equivalent-binary-trees

from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Recursive Solution:
    # Case 1: If both trees are empty, return True, if only one is, return False
    # Case 2: For every node, check recursively if the nodes left and right of it are the same,
    #         or whether they are flipped. If this is not the case for any node, False is returned
    #         for the whole method.
    def flipEquivRecursive(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return root1 == root2 is None
        return root1.val == root2.val and (
            self.flipEquivRecursive(root1.left, root2.left)
            and self.flipEquivRecursive(root1.right, root2.right)
            or self.flipEquivRecursive(root1.left, root2.right)
            and self.flipEquivRecursive(root1.right, root2.left))

    # Iterative Solution:
    # Use a Deque as a Queue using a BFS solution
    # Here, return False if the current popped elements of both deques are not equal.
    # As the code checks before adding whether the two values left of a node are equal and flips them
    # if not, if they are still not equal when popped it means that the tree was not just flipped on a given node.
    # Only one deque has to be flipped while the other stays the same for this to work though.
    def flipEquivIterative(self, root1: TreeNode, root2: TreeNode) -> bool:
        dq1, dq2 = map(collections.deque, ([root1], [root2]))
        while dq1 and dq2:
            node1, node2 = dq1.popleft(), dq2.popleft()
            if node1 == node2 is None:
                continue
            elif not node1 or not node2 or node1.val != node2.val:
                return False

            if node1.left == node2.left is None or node1.left and node2.left and node1.left.val ==  node2.left.val:
                dq1.extend([node1.left, node1.right])
            else:
                dq1.extend([node1.right, node1.left])
            dq2.extend([node2.left, node2.right])
        return not dq1 and not dq2

    # Helper function to check whether the traversal of a Tree in Leetcode yields the same
    # structure as locally, to apply the same tests.
    def traverse_tree(self, root: TreeNode):
        if not root:
            return []

        result = []
        queue = collections.deque([root])

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

        print(result)

        return result
