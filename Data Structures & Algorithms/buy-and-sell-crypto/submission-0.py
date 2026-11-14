class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = float("inf")
        max_profit = 0
        for i in prices:
            if i < mini : 
                mini = i
            else :
                if i - mini > max_profit:
                    max_profit = i - mini
        return max_profit