from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """递归判断二叉树是否轴对称。"""

        def is_mirror(left: Optional[TreeNode],
                      right: Optional[TreeNode]) -> bool: 
            # 两个空节点互为镜像。
            if left is None and right is None:
                return True

            # 只有一个为空，或者节点值不同，都不可能互为镜像。
            if left is None or right is None or left.val != right.val:
                return False

            # 外侧节点互相比较，内侧节点互相比较。
            return (is_mirror(left.left, right.right)
                    and is_mirror(left.right, right.left))

        return root is None or is_mirror(root.left, root.right)

    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        """使用队列迭代判断二叉树是否轴对称。"""
        if root is None:
            return True

        queue = [(root.left, root.right)]
        index = 0

        while index < len(queue):
            left, right = queue[index]
            index += 1

            if left is None and right is None:
                continue
            if left is None or right is None or left.val != right.val:
                return False

            # 按镜像位置将节点成对入队：外侧一对、内侧一对。
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))

        return True
