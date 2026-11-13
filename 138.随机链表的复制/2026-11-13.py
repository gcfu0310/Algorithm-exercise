from typing import Optional
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def copy(head:'Optional[Node]')->'Optional[Node]':
            if head is None:
                return None
            if head in hashmap:
                return hashmap[head]
            
            newNode=Node(head.val)
            hashmap[head]=newNode
            newNode.next=copy(head.next)
            newNode.random=copy(head.random)
            
            return newNode
        
        hashmap=dict()
        return copy(head)

            
        