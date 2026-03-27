def maxProfit(prices):
    res = 0
    lowest = prices[0]

    for price in prices:
        if price < lowest:
            lowest = price
        res = max(res, price - lowest)
        
    return res