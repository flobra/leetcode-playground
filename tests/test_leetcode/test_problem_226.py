from leetcode_problems.problem_226 import Solution
from data_structures.tree import list_to_tree, trees_are_equal

def test_invertTree():
    s = Solution()
	# Define test cases in the format: (tree, expected_result)
    test_cases = [
        ([1, 2, 3, 4, 5, 6, None, None, None, None, None, 7, 8], [1, 3, 2, None, 6, 5, 4, 8, 7]),
        ([], []),
        ([1, 2, 3], [1, 3, 2]),
        ([1], [1]),
        ([1, 2, 3, None, 4, 5, None, 6, None, 7, 8], [1, 3, 2, None, 5, 4, None, 8, 7, None, 6])
    ]

    # Run both flipEquivRecursive and flipEquivIterative on each test case
    for tree_input, expected_output in test_cases:

        tree = list_to_tree(tree_input)
        expected_output = list_to_tree(expected_output)

        # Test recursive version
        assert trees_are_equal(s.invertTree(tree), expected_output), f"Failed on recursive with input {tree}"

        # Initialize the tree once more as s.invertTree changes the Tree inplace
        tree = list_to_tree(tree_input)

        # Test iterative version
        assert trees_are_equal(s.invertTreeIterative(tree), expected_output), f"Failed on iterative with input {tree}"

