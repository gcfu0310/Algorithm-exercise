class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        max_profit = 0
        min_price = prices[0]
        for i in range(1,n):
            profit = prices[i]-min_price
            if profit>max_profit:
                max_profit = profit
            if prices[i]<min_price:
                min_price = prices[i]
        return max_profit