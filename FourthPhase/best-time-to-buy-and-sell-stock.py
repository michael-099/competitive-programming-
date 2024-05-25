class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell_pointer = 1
        buy_pointer = 0
        max_profit = 0

        while sell_pointer < len(prices):
            max_profit = max(max_profit, (prices[sell_pointer] - prices[buy_pointer]))
            if prices[buy_pointer] > prices[sell_pointer]:
                buy_pointer=sell_pointer 
            sell_pointer += 1

        return max_profit
