# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 验证BST的关键在于：递归维护一个区间
# 二叉搜索树的左子树所有节点的值都要小于根节点的值，右子树所有节点的值都要大于根节点的值
# 每遍历一个节点都要更新范围
# 时间复杂度是O(n),空间复杂度O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node,lower,upper):
            if node is None:
                return True
            if not (lower< node.val < upper):
                return False
            return helper(node.left,lower,node.val) and helper(node.right,node.val,upper)
        lower = float("-inf")
        upper = float("inf")
        return helper(root,lower,upper)

# 中序遍历的思想，一个二叉搜索树的中序遍历一定是一个升序序列
# 时间复杂度是O(n)，空间复杂度是O(n)，递归调用栈所占空间，最坏的情况就是退化成一个链表
    def isValidBST_2(self, root: Optional[TreeNode]) -> bool:
        lower = float("-inf")
        prev = lower
        def loop(root:Optional[TreeNode])->bool:
            nonlocal prev
            # 到底之后返回True
            if root is None:
                return True
            # 从后面返回的False一定要能传递
            if not loop(root.left):
                return False
            # 判断是否是升序的
            if root.val > prev:
                prev = root.val
            else:
                return False
            # 从后面返回的False一定要能传递
            if not loop(root.right):
                return False

            # 最终返回True
            return True
        return loop(root)