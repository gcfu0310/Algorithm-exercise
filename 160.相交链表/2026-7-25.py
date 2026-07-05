class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ha = headA
        hb = headB
        while ha != hb:
            ha = ha.next if ha else headB
            hb = hb.next if hb else headA
        return ha
    
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashmap = set()
        while headA != None:
            hashmap.add(headA)
            headA = headA.next
        while headB != None:
            if headB in hashmap:
                return headB
            headB = headB.next
        return None