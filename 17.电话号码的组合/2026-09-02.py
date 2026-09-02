from typing import List

class Solution:
    # 时间复杂度是O((3^m)*(4^n)),空间复杂度是O(m+n)
    def letterCombinations_1(self, digits: str) -> List[str]:
        n2c = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        def backtrack(i):
            if len(digits) == len(path):
                ans.append(''.join(path))
                return
            n = digits[i]
            cs = n2c[n]
            for c in cs:
                path.append(c)
                backtrack(i+1)
                path.pop()
        
        path = []
        ans = []  
        backtrack(0)
        return ans

    def letterCombinations_2(self, digits: str) -> List[str]:
        n2c = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        ans = n2c[digits[0]]
        if len(digits)==1:
            return ans
        for i in range(1,len(digits)):
            ans = [a+b for a in ans for b in n2c[digits[i]]]
        return ans