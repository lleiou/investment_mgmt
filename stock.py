def portfolio(purchase_history):
    """
    purchase_history: a python dictionary that follows the format of {symbol: [cost, share]}
        - symbol: symbol of the stock purchased
        - cost: price at the time of purchasing the stock
        - share: num of stocks purchased
    """
    profit = 0
    net_worth = 0
    for symbol in purchase_history:
        # generate a variable called price that is the current price of stock
        # (need to use beautiful soup to parse yahoo)
        cost =  purchase_history[symbol][0]
        share =  purchase_history[symbol][1]
        profit += (price-cost)*share
        net_worth += price*share
    return profit, net_worth