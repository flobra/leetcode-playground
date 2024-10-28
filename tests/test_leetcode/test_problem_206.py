import pytest
from leetcode_problems.problem_206 import Solution, ListNode

def list_to_linkedlist(lst):
    """Helper function to convert a list to a linked list."""
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(head):
    """Helper function to convert a linked list back to a Python list."""
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    return lst

@pytest.fixture
def solution():
    return Solution()

@pytest.mark.parametrize("input_list, expected_output", [
    ([], []),                       # empty list
    ([1], [1]),                     # single element list
    ([1, 2], [2, 1]),               # two element list
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),  # multiple elements
    ([1, 1, 1, 1], [1, 1, 1, 1]),   # all elements the same
])
def test_reverseListIterative(solution, input_list, expected_output):
    head = list_to_linkedlist(input_list)
    reversed_head = solution.reverseListIterative(head)
    output_list = linkedlist_to_list(reversed_head)
    assert output_list == expected_output, f"Failed on input: {input_list}"

@pytest.mark.parametrize("input_list, expected_output", [
    ([], []),                       # empty list
    ([1], [1]),                     # single element list
    ([1, 2], [2, 1]),               # two element list
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),  # multiple elements
    ([1, 1, 1, 1], [1, 1, 1, 1]),   # all elements the same
])
def test_reverseListRecursive(solution, input_list, expected_output):
    head = list_to_linkedlist(input_list)
    reversed_head = solution.reverseListRecursive(head)
    output_list = linkedlist_to_list(reversed_head)
    assert output_list == expected_output, f"Failed on input: {input_list}"

