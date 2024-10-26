# /leetcode_problems/problem_226.py
# Leetcode Problem #226: Invering Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/
from data_structures.tree import TreeNode
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return root

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root

    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.right, node.left])
        return root
