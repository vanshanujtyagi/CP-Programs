class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0] #the minimum value initially should be the first day price.
        profit = 0 #the initial profit should be zero
        for current_price in prices: #check for all prices.
            minimum = min(minimum, current_price) # min(a,b) returns the minimum between a and b. Thus, tell whether minimum is lesser or the current_price
            profit = max(profit, current_price - minimum) #max(a,b) returns the maximum between a and b. Thus, tell whether profit is greater or the current_price-minimum which is the current profit.
        return profit
