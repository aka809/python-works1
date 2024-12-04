user_input = input("Enter the stock prices separated by commas: ")
def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit

prices = list(map(int, user_input.split(',')))
result = max_profit(prices)
print(f"The maximum profit is: {result}")