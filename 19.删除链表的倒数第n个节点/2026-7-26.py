from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next
        target = length - n
        
        if target == 0:
            head = head.next
            return head
        
        num = 1
        cur = head
        while num != target:
            cur = cur.next
            num += 1
        cur.next = cur.next.next
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 构建虚假节点
        dummy = ListNode(0,head)
        stack = list()
        cur = dummy
        while cur is not None:
            stack.append(cur)
            cur = cur.next

        for i in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 构建虚假节点
        dummy = ListNode(0,head)
        first = head
        second = dummy
        for i in range(n):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next
