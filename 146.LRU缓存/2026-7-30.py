class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.use = []

    def get(self, key: int) -> int:
        if key in self.dict:
            index = self.use.index(key)
            self.use.pop(index)
            self.use.append(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 当待添加key未出现且未超出capacity
        if len(self.use) < self.capacity and key not in self.use:
            self.dict[key] = value
            self.use.append(key)

        # 当待添加的key已经出现在capacity
        elif key in self.use:
            self.dict[key] = value
            # 更新状态
            index = self.use.index(key)
            self.use.pop(index)
            self.use.append(key)

        # 当缓存数量超出capacity
        else:
            # 删除旧值以及记录
            del_key = self.use[0]
            self.use.pop(0)
            self.dict.pop(del_key)
            # 添加新值并添加记录
            self.dict[key] = value
            self.use.append(key)

# 哈希表+双链表
class Node:
    def __init__(self,key=None,val=None,prev=None,next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            # 删除该节点
            node.prev.next = node.next
            node.next.prev = node.prev

            # 尾部添加节点
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        # 添加新的键值对
        if len(self.dict.keys()) < self.capacity and key not in self.dict:
            self.dict[key] = Node(key,value,self.tail.prev,self.tail)
            self.tail.prev.next = self.dict[key]
            self.tail.prev = self.dict[key]

        # 键已经出现在现有的字典中时
        elif key in self.dict:
            node = self.dict[key]
            node.val = value

            # 删除该节点
            node.prev.next = node.next
            node.next.prev = node.prev

            # 尾部添加节点
            self.tail.prev.next = node
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev = node
        
        # 当添加数量后超过capacity
        else:
            # 待删除节点是头节点的下一个
            node = self.head.next

            # 得到待删除节点的key
            old_key = node.key

            # 在字典中删除这个节点
            self.dict.pop(old_key)

            # 在链表中删除这个节点
            node.prev.next = node.next
            node.next.prev = node.prev

            # 添加新节点
            self.dict[key] = Node(key,value,self.tail.prev,self.tail)
            self.tail.prev.next = self.dict[key]
            self.tail.prev = self.dict[key]



            
            