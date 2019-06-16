stocks = {
    'GOOG':489.45,
    'FB': 89.34,
    'AMZN':394.43,
    'YHOO':38.83,
    'AAPL': 102.34
}
print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))