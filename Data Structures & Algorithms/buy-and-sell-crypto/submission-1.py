class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        max_profits = 0 

        while R < len(prices):
            if prices[L] < prices[R]:
                if (prices[R]-prices[L]) > max_profits:
                    max_profits = prices[R]-prices[L]
            else:
                # found a lower buyer price
                L = R
            R += 1

        return max_profits




        

        
        