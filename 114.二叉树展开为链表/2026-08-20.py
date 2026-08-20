from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 时间复杂度是O(n)，空间复杂度是O(n+h)
    # 先采用先序遍历的方法遍历所有节点，此时获得顺序已经确定的列表
    # 接着遍历列表，把节点串起来就可以了
    # 优点：思路简单清晰，缺点：空间复杂度较高，需要O(n)空间去存储
    def flatten_0(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = list()
        def loop(node:Optional[TreeNode]):
            if node is None:
                return None
            ans.append(node)
            loop(node.left)
            loop(node.right)

        loop(root)

        for i in range(len(ans)-1):
            ans[i].right = ans[i+1]
            ans[i].left = None

    # 时间复杂度是O(n)，空间复杂度是O(h)
    """
    思考如何优化方法0中的方法，树一开始是未知形状的，从时间上进行优化比较困难，应该从空间上进行优化
    空间上应该优化方法0中的ans，采用常量空间来展开树
    直观地来看边遍历边对节点进行修改是最理想的状态，但是如果按照 根 → 左 → 右 的先序顺序，一边遍历一边直接修改 node.right = node.left，
    就可能覆盖原来的右子树，导致后续无法再访问它。
    所以改用逆先序 右 → 左 → 根。这样右子树会先处理完，prev 保存的是已经展开好的后续链表头节点。当处理当前节点时，只需要：
        node.right = prev
        node.left = None
        prev = node
    就不会丢失尚未遍历的节点
    """
    def flatten_1(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev= None
        def loop(node:Optional[TreeNode]):
            nonlocal prev
            if node is None:
                return None
            loop(node.right)
            loop(node.left)
            node.right = prev
            node.left = None
            prev = node

        loop(root)