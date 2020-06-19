def maxProfit(prices):
    if len(prices) ==0:
        return 0
    max_profit = 0
    for index, price in enumerate(prices):
        max_sell = max(prices[index:])
        profit = max_sell - price
        if profit > max_profit:
            max_profit = profit
    return max_profit

# fastest solution from leetcode
def maxProfitFast(prices):
    # very nice way to get to local minimum value.
    windowStart = 0
    n = len(prices)
    if not prices or n < 2:
        return 0

    maxProfit = 0
    for windowEnd in range(1, n):
        curProfit = prices[windowEnd] - prices[windowStart]
        if curProfit > maxProfit:
            maxProfit = curProfit
        elif prices[windowEnd] < prices[windowStart]:
            windowStart = windowEnd

    return maxProfit

if __name__ == '__main__':
    # prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]
    prices = [2,4,1,2]
    print(maxProfitFast(prices))