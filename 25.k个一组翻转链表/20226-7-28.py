from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 判断剩余链表长度是否符合翻转要求
        check = head
        for _ in range(k):
            if not check:
                return head
            check = check.next

        prev = None
        cur = head
        for _ in range(k):
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        head.next = self.reverseKGroup(cur,k)

        return prev