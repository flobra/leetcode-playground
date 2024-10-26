from leetcode_problems.problem_1448 import Solution
from data_structures.tree import list_to_tree

def test_invertTree():
    s = Solution()
	# Define test cases in the format: (tree, expected_result)
    test_cases = [
        ([3,1,4,3,None,1,5], 4),
        ([], None),
        ([1, 2, 3], 3),
        ([1], 1)
    ]

    # Run both flipEquivRecursive and flipEquivIterative on each test case
    for tree_input, expected_output in test_cases:

        tree = list_to_tree(tree_input)

        # Test recursive version
        assert s.goodNodes(tree) == expected_output, f"Failed on recursive with input {tree}"

