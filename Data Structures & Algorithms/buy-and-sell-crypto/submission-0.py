class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        curr_max = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                curr_max = max(curr_max, profit)
            else:
                l = r
            r += 1
        return curr_max