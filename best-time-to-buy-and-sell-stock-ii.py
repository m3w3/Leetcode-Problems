"""
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        
        # handle initial case
        if prices[0] < prices[1]:
            if n == 2: return prices[1] - prices[0]
            profit, has_stock = -prices[0], True
        else:
            if n == 2: return 0
            profit, has_stock = 0, False
        
        # handle middle case
        for i in range(1, n - 1):
            if prices[i] == prices[i + 1]:
                continue
            # valley
            elif (not has_stock) and is_valley(prices, i):
                profit -= prices[i]
                has_stock = True
            # peak
            elif (has_stock) and is_peak(prices, i):
                profit += prices[i]
                has_stock = False
        
        # handle final case
        if has_stock:
            return profit + prices[i + 1]

        return profit

    
def is_peak(prices, i):
    return prices[i - 1] <= prices[i] and prices[i] > prices[i + 1]

def is_valley(prices, i):
    return prices[i - 1] >= prices[i] and prices[i] < prices[i + 1]
