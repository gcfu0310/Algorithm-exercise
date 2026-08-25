from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        D = 0
        def helper(node):
            nonlocal D
            if node is None:
                return 0
            left_depth = helper(node.left)
            right_depth = helper(node.right)
            D = max(D,left_depth+right_depth)
            return max(left_depth,right_depth)+1
        helper(root)
        return D