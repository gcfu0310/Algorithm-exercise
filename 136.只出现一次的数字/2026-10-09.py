from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        xor异或运算,任何数与0做异或等于它自身,任何数和他自己做异或等于0
        xor满足交换律,例如:a^b^a,可以改为:a^a^b=b
        一组数字只有一个数字出现一次,其他数字都是出现两次,交换之后,计算出来一定是只出现一次的那个数
        """
        ans = 0
        for num in nums:
            ans ^= num
        return ans