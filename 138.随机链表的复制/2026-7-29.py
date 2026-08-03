from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next

class Solution:
    # 笨蛋方法
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        newHead = Node(0)
        cur = newHead
        cur_head = head
        newHeads = dict()
        head_num = dict() # 给原链表各个元素排序
        i = 0

        # 复制链表的val和next，构建链表index -> node的字典
        while cur_head is not None:
            node = Node(cur_head.val)
            head_num[cur_head] = i
            cur.next = node

            cur = cur.next
            newHeads[i] = cur
            cur_head = cur_head.next
            i += 1

        cur_head = head
        randoms = list()
        while cur_head is not None:
            if cur_head.random is None:
                randoms.append(None)
                cur_head = cur_head.next
                continue

            randoms.append(head_num[cur_head.random])
            cur_head = cur_head.next
        
        cur = newHead.next
        i = 0
        while cur is not None and i < len(randoms):
            if randoms[i] is None:
                cur = cur.next
                i += 1
                continue
            
            cur.random = newHeads[randoms[i]]
            cur = cur.next
            i += 1

        return newHead.next
    
    # 哈希表，构建旧节点->新节点的字典
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return None
        
        # 构建哈希表
        cur = head
        hashmap = dict()
        while cur is not None:
            hashmap[cur] = Node(cur.val)
            cur = cur.next
        
        # 完成next和random
        cur = head
        while cur is not None:
            hashmap[cur].next = hashmap.get(cur.next)
            hashmap[cur].random = hashmap.get(cur.random)
            cur = cur.next
        
        return hashmap[head]
    
    # 递归+哈希
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.visited = dict()
        return self.copy(head)
        
        def copy(self,head:Optional[Node]) -> Optional[Node]:
            # 递归终止条件
            if head is None:
                return None
            if head in self.visited:
                return self.visited[head]

            # 本层解决的问题
            newNode = Node(head.val)
            self.visited[head] = newNode
            newNode.next = self.copy(head.next)
            newNode.random = self.copy(head.random)

            # 返回对应的值
            return newNode