from leetcode_problems.problem_951 import Solution, TreeNode
from typing import Optional, List
from collections import deque

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

def test_flipEquiv():
    s = Solution()
	# Define test cases in the format: (tree1, tree2, expected_result)
    test_cases = [
        ([1, 2, 3, 4, 5, 6, None, None, None, 7, 8], [1, 3, 2, None, 6, 4, 5, None, None, None, None, 8, 7], True),
        ([], [], True),
        ([], [1], False),
        ([1], [1], True),
        ([1], [2], False),
        ([1, 2], [1, None, 2], True),
        ([1, 2, 3, 4, None, None, 5, 6, None, None, 7], [1, 3, 2, None, 5, 4, None, None, 7, 6, None], True),
        ([1, 2, None, 3, None, None, 4], [1, None, 2, None, 3, 4, None], True),
        ([1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, 10, 11], [1, 3, 2, 7, 6, 5, 4, 11, 10, None, None, 9, 8], True),
        ([1, 2, None, 3, None, None, 4], [1, None, 2, None, 3, 4], True)
    ]

    # Run both flipEquivRecursive and flipEquivIterative on each test case
    for tree1_list, tree2_list, expected in test_cases:
        tree1 = list_to_tree(tree1_list)
        tree2 = list_to_tree(tree2_list)

        # Test recursive version
        assert s.flipEquivRecursive(tree1, tree2) == expected, f"Failed on recursive with input {tree1_list} and {tree2_list}"

        # Test iterative version
        assert s.flipEquivIterative(tree1, tree2) == expected, f"Failed on iterative with input {tree1_list} and {tree2_list}"

