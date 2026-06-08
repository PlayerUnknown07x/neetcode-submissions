class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = prices[0]
        for price in prices:
            profitA = price - minimum
            profit = max (profit,profitA)
            minimum = min(minimum,price)
        return profit

        
        