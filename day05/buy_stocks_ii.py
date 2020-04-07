"""
Prompt:
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

# Runs in O(n) time and O(1) space. Involves a silding window technique


def max_profit(prices):
    if len(prices) == 0:
        return 0
    cur_num = prices[0]
    price_sum = 0
    index = 0
    while index < len(prices):
        if index + 1 >= len(prices):
            break
        elif cur_num > prices[index + 1]:
            cur_num = prices[index + 1]
        else:
            if index + 2 < len(prices):
                if prices[index + 1] > prices[index + 2]:
                    price_sum += (prices[index + 1] - cur_num)
                    cur_num = prices[index + 2]
                    index += 1
            else:
                price_sum += (prices[index + 1] - cur_num)
        index += 1
    return price_sum


# Test Cases
print(max_profit([7, 1, 5, 3, 6, 4]))
# Profit is 7 as Buy on day 2 (price = 1)
# and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on day 4 (price = 3)
# and sell on day 5 (price = 6), profit = 6-3 = 3.

print(max_profit([7, 6, 4, 3, 1]))
# Profit is 0
# In this case, no transaction is done, i.e. max profit = 0.
