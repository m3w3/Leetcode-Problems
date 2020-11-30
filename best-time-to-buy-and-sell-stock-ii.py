class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        
        # handle initial case
        if prices[0] < prices[1]:
            if n == 2: return prices[1] - prices[0]
            profit = -prices[0]
            has_stock = True
        else:
            if n == 2: return 0
            profit = 0
            has_stock = False
        
        # handle middle case
        for i in range(1, n - 1):
            if prices[i] == prices[i + 1]:
                continue
            # valley
            elif prices[i - 1] >= prices[i] and prices[i] < prices[i + 1]:
                if not has_stock:
                    profit -= prices[i]
                    has_stock = True
            # peak
            elif prices[i - 1] <= prices[i] and prices[i] > prices[i + 1]:
                if has_stock:
                    profit += prices[i]
                    has_stock = False
        
        # handle final case
        if has_stock:
            return profit + prices[i + 1]
​
        return profit
