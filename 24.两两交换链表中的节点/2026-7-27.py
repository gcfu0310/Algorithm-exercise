from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

# val交换迭代
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fisrt = head
        if fisrt is None:
            return head
        second = head.next
        while fisrt and second:
            val = fisrt.val
            fisrt.val = second.val
            second.val = val
            if second.next is None:
                break
            else:
                fisrt = second.next
                second = second.next.next
        return head

# 迭代
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        temp = dummy
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1
        return dummy.next

# 递归
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        newHead = head.next
        head.next = self.swapPairs(newHead.next)
        newHead.next = head
        return newHead