# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 哈希 (时间复杂度O(n),空间复杂度O(n))
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sets = set()
        while head != None:
            if head in sets:
                return head
            if head not in sets:
                sets.add(head)
            head = head.next
        return None
    
# 答辩标记（改变了原链表，时间复杂度O(n),空间复杂度降到了O(1)）
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head is not None:
            if head.val is None:
                return head
            head.val = None
            head = head.next
        return None
    
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None