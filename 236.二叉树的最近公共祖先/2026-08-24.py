class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root:"TreeNode"):
            if root is None:
                return None
            if root == p or root == q: # 当前节点就是 p/q，向上返回这个有效节点
                return root
            # # 获取左右子树返回的有效结果
            left = helper(root.left) 
            right = helper(root.right) 

            # 左右子树都有有效结果，
            # 说明 p 和 q 在当前节点两侧，当前节点就是 LCA
            if left and right:
                return root

            # 只有一边有有效结果，则继续向上传递
            # 这个结果可能是 p/q，也可能已经是 LCA
            return left if left else right
        
        return helper(root)