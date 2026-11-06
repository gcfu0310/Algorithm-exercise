from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 翻转链表
        def reverse(head:Optional[ListNode])->Optional[ListNode]:
            pre=None
            cur=head
            while cur is not None:
                temp=cur.next
                cur.next=pre
                pre=cur
                cur=temp
            return pre
        # 快慢指针，链表长度为偶数时，slow指针刚好走到链表的一半处
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # 链表长度为奇数，slow指针刚好走到中间的位置，fast走到链表最后一个位置
        if fast:
            slow=slow.next
        left=head
        # 翻转后一半链表，与前一半链表进行比较
        right=reverse(slow)
        while right is not None:
            if right.val!=left.val:
                return False
            left=left.next
            right=right.next
        return True