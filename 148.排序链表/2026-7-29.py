# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 合并两个有序链表
        def merge(left,right):
            ans = ListNode(0)
            cur = ans
            while left is not None and right is not None:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                    cur = cur.next
                else:
                    cur.next = right
                    right = right.next
                    cur = cur.next
            cur.next = left if left else right
            return ans.next
        
        # 终止条件
        if head is None or head.next is None:
            return head
        
        # 找中点（最后的slow.next就是中点）
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 定义左右两个链表的头节点，以及左链表的尾节点
        left_head = head
        right_head = slow.next
        slow.next = None

        left = self.sortList(left_head)
        right = self.sortList(right_head)

        return merge(left,right)
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 合并两个有序链表
        def merge(left,right):
            ans = ListNode(0)
            cur = ans
            while left is not None and right is not None:
                if left.val < right.val:
                    cur.next = left
                    left = left.next
                    cur = cur.next
                else:
                    cur.next = right
                    right = right.next
                    cur = cur.next
            cur.next = left if left else right
            return ans.next
        
        # 空链表
        if head is None:
            return head
        
        # 计算链表长度
        cur = head
        length = 0
        while cur is not None:
            length += 1
            cur = cur.next
        
        # sublength
        sublength = 1
        dummyHead = ListNode(0,head)
        while sublength < length:
            prev,curr = dummyHead,dummyHead.next
            while curr:
                head1 = curr
                for _ in range(1,sublength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for _ in range(1,sublength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                succ = None
                if curr:
                    succ = curr.next
                    curr.next = None
                
                merged = merge(head1,head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            sublength <<= 1
        return dummyHead.next
                    
