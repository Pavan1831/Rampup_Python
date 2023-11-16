def max_profit(stock_prices):
    if len(stock_prices) < 2:
        return "Not enough data to make a profit."

    profit = 0
    buying_day = 0
    max_profit_days = []

    for i in range(1, len(stock_prices)):
        if stock_prices[i] > stock_prices[i - 1]:
            continue
        else:
            if buying_day < i - 1:
                profit += stock_prices[i - 1] - stock_prices[buying_day]
                max_profit_days.append((buying_day, i - 1))
            buying_day = i

    if buying_day < len(stock_prices) - 1:
        profit += stock_prices[-1] - stock_prices[buying_day]
        max_profit_days.append((buying_day, len(stock_prices) - 1))

    #print(max_profit_days)

    if profit > 0:
        result = []
        for start, end in max_profit_days:
            buying_price = stock_prices[start]
            selling_price = stock_prices[end]
            result.append(f"Buy stock on day {start + 1} at INR: {buying_price} and sell on day {end + 1} at INR: {selling_price}")

        return result
    else:
        return "No profit can be made with these stock prices."

stock_prices = [100, 20, 260, 310, 40, 535, 20]
result = max_profit(stock_prices)

if isinstance(result, list):
    for item in result:
        print(item)
else:
    print(result)
