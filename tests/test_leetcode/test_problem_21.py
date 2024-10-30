from leetcode_problems.problem_21 import Solution, ListNode

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list of values for easy assertion
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Test cases for mergeTwoLists
def test_both_empty():
    assert Solution().mergeTwoLists(None, None) is None

def test_first_empty():
    list2 = create_linked_list([1, 3, 4])
    merged_list = Solution().mergeTwoLists(None, list2)
    assert linked_list_to_list(merged_list) == [1, 3, 4]

def test_second_empty():
    list1 = create_linked_list([1, 2, 4])
    merged_list = Solution().mergeTwoLists(list1, None)
    assert linked_list_to_list(merged_list) == [1, 2, 4]

def test_equal_sized_lists():
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    merged_list = Solution().mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged_list) == [1, 1, 2, 3, 4, 4]

def test_different_sized_lists():
    list1 = create_linked_list([1, 3, 5])
    list2 = create_linked_list([2, 4, 6, 8, 10])
    merged_list = Solution().mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged_list) == [1, 2, 3, 4, 5, 6, 8, 10]

def test_lists_with_duplicates():
    list1 = create_linked_list([1, 2, 4, 4])
    list2 = create_linked_list([1, 3, 4, 5])
    merged_list = Solution().mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged_list) == [1, 1, 2, 3, 4, 4, 4, 5]

def test_large_values():
    list1 = create_linked_list([1000, 2000, 3000])
    list2 = create_linked_list([1500, 2500, 3500])
    merged_list = Solution().mergeTwoLists(list1, list2)
    assert linked_list_to_list(merged_list) == [1000, 1500, 2000, 2500, 3000, 3500]
    