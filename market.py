import random


def get_price(symbol):

    prices = {

        "AAPL": 195,
        "NVDA": 180,
        "MSFT": 420,
        "BTC": 67000,
        "ETH": 3500

    }


    if symbol in prices:
        return prices[symbol]


    return random.randint(10,500)
