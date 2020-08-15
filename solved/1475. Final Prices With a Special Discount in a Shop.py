# New Method
# order N, one single pass with nester while loop, another list comprehension
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discount = {}
        for i in range(len(prices)):
            op = prices[i]
            j = i + 1
            while j < len(prices):
                d = prices[j]
                if d <= op:
                    discount[i] = d
                    break
                j += 1
            else:
                discount[i] = 0
        return [prices[i] - discount[i] for i in range(len(prices))]

# Improvement in last solution
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        discount = {}
        for i in range(len(prices)):
            op = prices[i]
            j = i+1
            while j < len(prices):
                d = prices[j]
                if d <= op:
                    # can update value here only
                    prices[i] = prices[i] - d
                    break
                j += 1
        return prices

    # the same method can be presented with the idea of stack
    def finalPricesStack(self, prices: List[int]) -> List[int]:
        res, stack = prices[:], []
        for i, price in enumerate(prices):
            while stack and prices[stack[-1]] >= price:
                res[stack.pop()] -= price
            stack.append(i)
        return res



def finalPrices(prices):
    new_prices = prices[:]
    final_cost = []
    for price in prices:
        new_prices.pop(0)
        flag = True
        if len(new_prices) ==0:
            final_cost.append(price)
        else:
            for new_price in new_prices:
                if new_price <= price:
                    final_cost.append(price - new_price)
                    flag = False
                    break
            if flag:
                final_cost.append(price)
    return final_cost
# best solution on leetcode

def finalPricesBest(prices):
    ans = []
    for i in range(len(prices)):
        m = prices[i]
        flag = False
        for j in range(i + 1, len(prices)):
            if m >= prices[j]:
                flag = True
                m = prices[j]
                break
        if flag:
            ans.append(prices[i] - m)
        else:
            ans.append(prices[i])
    return ans


if __name__ == '__main__':
    # prices = [8, 4, 6, 2, 3]
    # prices = [1, 2, 3, 4, 5]
    prices = [10, 1, 1, 6]
    print(finalPrices(prices))

