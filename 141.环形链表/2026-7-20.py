from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle_hashmap(self, head: Optional[ListNode]) -> bool:
        hashmap = set()
        cur_node = head
        while cur_node is not None:
            if cur_node in hashmap:
                return True
            hashmap.add(cur_node)
            cur_node = cur_node.next
        return False

    def hasCycle_slow_fast_pointer(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False