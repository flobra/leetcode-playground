# /leetcode_problems/problem_21.py
# Solution for Leetcode Problem #21: Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = temp = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else: 
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        temp.next = list1 or list2
        return dummy.next