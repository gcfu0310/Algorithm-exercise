class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        w_max = 0
        while i != j:
            if height[i] < height[j]:
                w = (j - i) * height[i]
                i += 1
            else:
                w = (j - i) * height[j]
                j -= 1
            if w > w_max:
                w_max = w
        return w_max