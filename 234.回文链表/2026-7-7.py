from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""温习之前写的翻转链表的方法基础之上进行拓展"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverseList_savehead(head):
            prev = None
            curr = head
            newhead = ListNode(-1)
            tmp = newhead
            while curr != None:
                """先复制原链表"""
                tmp.next = ListNode(curr.val)
                tmp = tmp.next
                """再翻转链表"""
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            newhead = newhead.next
            return newhead,prev
        newhead,reverse_head = reverseList_savehead(head)
        while newhead != None and reverse_head != None:
            if newhead.val != reverse_head.val:
                return False
            newhead = newhead.next
            reverse_head = reverse_head.next
        return True

"""将内容复制到数组中并利用双指针的方法"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reverse = []
        while head != None:
            reverse.append(head.val)
            head = head.next
        return reverse == reverse[::-1]
    
"""递归（感觉好麻烦）"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()

"""快慢指针"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def end_of_first_half(head):
            """快慢指针，慢指针走一步，快指针走两步，当快指针走到尾部时，慢指针走到链表中间"""
            slow = head 
            fast = head
            while fast.next and fast.next.next is not None:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverselist(head):
            """翻转链表"""
            prev = None
            curr = head
            while curr != None:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        
        
        first_half_end = end_of_first_half(head)
        second_half_start = reverselist(first_half_end.next)

        result = True 
        second_position = second_half_start
        while head and second_position is not None:
            if head.val != second_position.val:
                result = False
            head = head.next
            second_position= second_position.next
        return result
"""
class Solution:
    def end_of_first_half(self,head):
        slow = head 
        fast = head
        # while slow.next and fast.next.next is not None:
        while fast.next and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def reverselist(self,head):
        prev = None
        curr = head
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
             
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverselist(first_half_end.next)

        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                return False
            first_position = first_position.next
            second_position = second_position.next
        first_half_end.next = self.reverselist(second_half_start)
        return result
"""