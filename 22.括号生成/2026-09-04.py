from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        ans = []
        # left和right来记录path中已有的左括号与右括号数量
        def backtrack(left,right):
            # 终止条件
            if right == left == n:
                ans.append(''.join(path))
                return
            # 添加左括号的时机
            if left < n:
                path.append('(')
                backtrack(left+1,right)
                path.pop()
            # 添加右括号的时机
            if right < left:
                path.append(')')
                backtrack(left,right+1)
                path.pop()
        backtrack(0,0)
        return ans

        