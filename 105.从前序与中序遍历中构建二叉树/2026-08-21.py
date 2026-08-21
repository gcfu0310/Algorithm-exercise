# Definition for a binary tree node.
from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
思路解析：
有前序和中序遍历的数组，首先前序数组的第一个元素一定是树的根节点值(node_val)，接着在中序数组中找到这个根节点值对应的下标(root_index)，最后
就可以在前序和中序数组中切分成左子树和右子树。这种典型的重复操作，就可以联想到用递归来解决。
"""
class Solution:
    # 方法0采用的是递归数组的形式，每次递归切片好的左子树的前序数组和中序数组以及右子树的前序数组和中序数组
    # 空间复杂度O(n^2),时间复杂度O(n^2),优点：简明清晰；缺点：时间和空间上的复杂度较高，较高的原因是：时间上主要是找index下标，空间上则是反复的创造切片
    def buildTree_0(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        in_ltree = inorder[:root_index]
        in_rtree = inorder[root_index+1:]
        pre_ltree = preorder[1:len(in_ltree)+1]
        pre_rtree = preorder[len(in_ltree)+1:]
        root.left = self.buildTree(pre_ltree,in_ltree)
        root.right = self.buildTree(pre_rtree,in_rtree)
        return root

    # 方法1针对方法0的痛点，做了以下改进：（总体思路不变）
    # 在时间上，提前创建哈希表用来存储中序数组的值以及对应的下标，将这一步的时间复杂度降低到O(1)
    # 在空间上，递归不再传递切片，而是传递左子树在前序和中序数组中的左右两个指针，也就是维护左子树这个范围，右子树同理，进而降低空间复杂度
    # 时间复杂度:O(n),空间复杂度:O(n)

    def buildTree_1(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = dict()
        for i in range(len(inorder)):
            inorder_map[inorder[i]] = i
        def helper(pre_left:int,pre_right:int,in_left:int,in_right:int):
            if pre_left > pre_right:
                return None
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            root_index = inorder_map[root_val] # 找到root值对应的下标
            left_len = root_index - in_left # 计算左子树的长度
            root.left = helper(pre_left+1,pre_left+left_len,in_left,root_index-1)
            root.right = helper(pre_left+left_len+1,pre_right,root_index+1,in_right)
            return root
        return helper(0,len(preorder)-1,0,len(inorder)-1)

    