# Best Stock
'''
You are given the current stock prices.
You have to find out which stocks cost more.
Input: The dictionary where the market identifier code is a key and the value is a stock price.
Output: The market identifier code (ticker symbol) as a string.
'''

def best_stock(stocks):
    best_price = 0
    for name_stock in stocks:
        if stocks[name_stock] > best_price:
            best_name = name_stock
            best_price = stocks[name_stock]
    return best_name


print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))     # "ATX"
print(best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}))   # "TASI"


# max(data.values())

def best_stock(data):
    for stock in data:
        if data[stock] == max(data.values()):
            return stock

# next sample
def best_stock(a):
    return max(a, key=a.get)