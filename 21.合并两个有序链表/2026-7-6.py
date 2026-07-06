from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode(-1)
        k = pre
        while list1 and list2:
            if list1.val < list2.val:
                k.next = list1
                list1 = list1.next
                k = k.next
            else:
                k.next = list2
                list2 = list2.next
                k = k.next
        k.next = list1 if list1 else list2
        return pre.next