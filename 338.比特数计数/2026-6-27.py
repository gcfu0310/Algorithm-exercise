class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n+1):
            c = 0
            t = num
            while t / 2 != 0:
                k = mod(t,2)
                if k == 1:
                    c+=1
                t = t // 2
            ans.append(c)
        return ans