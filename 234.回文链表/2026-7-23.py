# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        return values == values[::-1]

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front_head = head
        def check(cur_node=head):
            if cur_node:
                if not check(cur_node.next):
                    return False
                if self.front_head.val != cur_node.val:
                    return False
                self.front_head = self.front_head.next
            return True
        return check()