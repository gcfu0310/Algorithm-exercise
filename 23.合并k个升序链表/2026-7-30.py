# Definition for singly-linked list.
from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #  顺序合并
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(head1,head2):
            ans = ListNode(0)
            cur = ans
            while head1 and head2:
                if head1.val < head2.val:
                    cur.next = head1
                    cur = cur.next
                    head1 = head1.next
                else:
                    cur.next = head2
                    cur = cur.next
                    head2 = head2.next
            cur.next = head1 if head1 else head2
            return ans.next
        
        # 当列表为空时
        n = len(lists)
        if n == 0:
            return None

        ans = lists[0]
        for i in range(1,n):
            ans = merge(ans,lists[i])
        return ans

    # 分治合并
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(head1,head2):
            ans = ListNode(0)
            cur = ans
            while head1 and head2:
                if head1.val < head2.val:
                    cur.next = head1
                    cur = cur.next
                    head1 = head1.next
                else:
                    cur.next = head2
                    cur = cur.next
                    head2 = head2.next
            cur.next = head1 if head1 else head2
            return ans.next

        def merged(lists,left,right):
            if left == right:
                return lists[left]
            if left > right:
                return None
            mid = (left+right) // 2
            return merge(merged(lists,left,mid),merged(lists,mid+1,right))

        return merged(lists,0,len(lists)-1)