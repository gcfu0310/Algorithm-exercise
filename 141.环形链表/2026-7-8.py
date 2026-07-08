# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """哈希表"""
        hashmap = set()
        while head != None:
            if head  in hashmap:
                return True
            hashmap.add(head)
            head = head.next
        return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """快慢指针"""
        # 空链表以及链表中只有一个元素的情况
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            # 不存在cycle时，fast指针会快于slow到达链表末尾，直接返回False
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        # 当两个指针重合，说明存在cycle
        return True

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """撒尿标记法"""
        # 链表为空的情况
        if head is None:
            return False
        
        while head.next is not None:
            head.val=None
            head=head.next
            if head.val is None:
                return True
        return False