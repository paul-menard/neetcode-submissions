class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # int : profit
        # k : tracks where the window is

        n = len(prices)
        profit = 0 
        for k in range(n-1):
            if prices[k] < prices[k+1]:
                profit += prices[k+1] - prices[k]
        return profit

