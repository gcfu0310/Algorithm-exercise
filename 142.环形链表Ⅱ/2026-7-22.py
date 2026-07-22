from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                ptr = head
                while slow != ptr:
                    slow = slow.next
                    ptr = ptr.next
                return slow
        return 

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        hashmap = set()
        while cur is not None:
            if cur in hashmap:
                return cur
            hashmap.add(cur)
            cur = cur.next
        return 