from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode_pointer(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        start_A,start_B = headA,headB
        cur_A,cur_B = headA,headB
        Flag_A,Flag_B = True,True
        while cur_A != cur_B:
            cur_A = cur_A.next
            cur_B = cur_B.next
            if cur_A == None and Flag_A:
                cur_A = start_B
                Flag_A = False
            if cur_B == None and Flag_B:
                cur_B = start_A
                Flag_B = False
        return cur_A
    
    def getIntersectionNode_hashmap(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hasmap = set()
        while headA is not None:
            hasmap.add(headA)
            headA = headA.next
        while headB is not None:
            if headB in hasmap:
                return headB
            headB = headB.next