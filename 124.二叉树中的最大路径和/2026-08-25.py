from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 题外话：求二叉树所有元素的和 时间复杂度是O(n)，空间复杂度是O(1)
def Sum_Tree(root:TreeNode)->int:
    def helper(root:TreeNode)->int:
        if root is None:
            return 0
        left_gain = helper(root.left)
        right_gain = helper(root.right)
        return root.val+left_gain+right_gain
    return helper(root)

class Solution:
    # 时间复杂度是O(n),空间复杂度是O(h)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def helper(node:Optional[TreeNode])->int:
            nonlocal max_sum
            if node is None:
                return 0
            left_gain = max(helper(node.left),0) # 左子树的有效值，如果是负数，就记为0，代表路径不经过
            right_gain = max(helper(node.right),0) # 右子树的有效值，如果是负数，就记为0，代表路径不经过
            curr_sum = node.val+left_gain+right_gain # 过当前节点双分支下的最大和
            max_sum = max(curr_sum,max_sum) # 更新最大路径和
            return node.val+max(left_gain,right_gain) # 返回经过该节点单分支下的最大路径和
        helper(root)
        return max_sum
