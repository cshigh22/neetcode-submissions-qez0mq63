class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0

        for i in range(left + 1, len(prices)):
            profit = max(profit, prices[i] - prices[left])
            if prices[left] > prices[i]:
                left = i
        return profit

            