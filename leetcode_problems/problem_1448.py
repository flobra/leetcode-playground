# /leetcode_problems/problem_1448.py
# Leetcode Problem #1448: Count Good Nodes in Binary Tree
#
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

from data_structures.tree import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return None

        def count(node: TreeNode, maximum: int):
            if not node:
                return 0

            mx = max(node.val, maximum)

            return (node.val >= maximum) + count(node.left, mx) + count(node.right, mx)

        return count(root, root.val)
