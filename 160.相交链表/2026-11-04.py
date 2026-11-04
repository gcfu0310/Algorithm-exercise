from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def getIntersectionNode_1(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 哈希表 时间复杂度:O(m+n),空间复杂度:O(m)
        hashmap=set()
        cur=headA
        while cur is not None:
            hashmap.add(cur)
            cur=cur.next
        cur=headB
        while cur is not None:
            if cur in hashmap:
                return cur
            cur=cur.next
        return None

    def getIntersectionNode_2(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # 时间复杂度O(m+n),空间复杂度O(1)
        # 当两个链表相交，必定在相交点重合；当两个链表不相交，两个指针必定同时指向None
        # m+n=n+m A走到A的尾，切换到B的头，B走到B的尾，切换到A的头
        cur_A,cur_B = headA,headB
        while cur_A != cur_B:
            cur_A=cur_A.next if cur_A else headB
            cur_B=cur_B.next if cur_B else headA
        return cur_A
