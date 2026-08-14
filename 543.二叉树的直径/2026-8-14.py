from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 时间复杂度是O(n),空间复杂度是O(h)，主要是递归过程分配的栈空间
    # 计算二叉树直径的方法就是遍历每个节点，计算经过该节点最长路径，最后筛选出最长的路径即为直径
    # 经过该节点的最长路径等于left_max_depth+right_max_depth
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        D = 0
        def max_depth(root:Optional[TreeNode]) -> int:
            nonlocal D
            if root is None:
                return 0
            left_depth = max_depth(root.left)
            right_depth = max_depth(root.right)
            D = max(D,left_depth+right_depth)
            return max(left_depth,right_depth)+1
        max_depth(root)
        return D