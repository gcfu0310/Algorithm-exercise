# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 时间复杂度是O(n^2),空间复杂度是O(h)
    def pathSum_1(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def countPathSum(root,targetSum):
            nonlocal count
            if root is None:
                return 
            if root.val == targetSum:
                count += 1
            countPathSum(root.left,targetSum-root.val)
            countPathSum(root.right,targetSum-root.val)
        
        def helper(root,targetSum):
            if root is None:
                return None
            countPathSum(root,targetSum)
            helper(root.left,targetSum)
            helper(root.right,targetSum)
        
        helper(root,targetSum)
        return count

    # 时间复杂度是O(n),空间复杂度是O(h)
    def pathSum_2(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        prefix_count = {0:1} # 防止出现这个数就是targetSum的情况
        def dfs(root, current_sum):
            nonlocal count,prefix_count
            if root is None:
                return

            # 计算当前的前缀和
            current_sum += root.val

            # prefix_sum[j] - prefix_sum[i] == targetSum，说明序列[i,j]之间数组和为targetSum
            need = current_sum - targetSum
            # 此处相当于判断prefix_sum[i]是否存在以及存在几次，存在的话就将存在次数加到count中，存在次数就说明有几个
            count += prefix_count.get(need, 0)

            # 将当前的前缀和添加到记录中
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

            # 递归左右子树
            dfs(root.left, current_sum)
            dfs(root.right, current_sum)

            # 回溯的时候，需要去掉这次前缀和的记录，否则前缀和就不等于当前的路径和了
            prefix_count[current_sum] -= 1

        dfs(root,0)
        return count


        