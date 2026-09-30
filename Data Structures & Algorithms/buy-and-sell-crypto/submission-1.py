class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy_amt = prices[0]
        max_profit = 0

        for day, amt in enumerate(prices):
            max_profit = max(max_profit, amt - min_buy_amt)
            min_buy_amt = min(min_buy_amt, amt)
        
        return max_profit