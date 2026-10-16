class Asset:
    def __init__(self, symbol, quantity, buy_price):
        self.symbol = symbol
        self.quantity = quantity
        self.buy_price = buy_price

    def value(self, current_price):
        return self.quantity * current_price

    def profit(self, current_price):
        return (current_price - self.buy_price) * self.quantity


class Portfolio:
    def __init__(self):
        self.assets = []


    def add_asset(self, symbol, quantity, buy_price):
        asset = Asset(symbol, quantity, buy_price)
        self.assets.append(asset)


    def remove_asset(self, symbol):
        self.assets = [
            asset for asset in self.assets
            if asset.symbol != symbol
        ]


    def total_invested(self):
        total = 0

        for asset in self.assets:
            total += asset.quantity * asset.buy_price

        return total


    def total_value(self, prices):
        total = 0

        for asset in self.assets:
            if asset.symbol in prices:
                total += asset.quantity * prices[asset.symbol]

        return total


    def total_profit(self, prices):
        return self.total_value(prices) - self.total_invested()
