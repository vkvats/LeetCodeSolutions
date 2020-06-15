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

