# /leetcode_problems/problem_206.py
# Solution for Leetcode Problem #206: Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseListIterative(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        prev = None

        #loop
        while head.next:
            cache = head.next
            head.next = prev
            prev = head
            head = cache

        head.next = prev

        return head 

    def reverseListRecursive(self, head: Optional[ListNode], prev: Optional[ListNode] = None) -> Optional[ListNode]:

        if not head:
            return prev

        cache = head.next        
        head.next = prev

        return self.reverseListRecursive(cache, head)
    