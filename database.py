import json


def save_portfolio(portfolio):

    data = []

    for asset in portfolio.assets:
        data.append({
            "symbol": asset.symbol,
            "quantity": asset.quantity,
            "buy_price": asset.buy_price
        })


    with open("portfolio.json", "w") as file:
        json.dump(data, file, indent=4)



def load_portfolio(portfolio):

    try:

        with open("portfolio.json") as file:
            data = json.load(file)


        for asset in data:
            portfolio.add_asset(
                asset["symbol"],
                asset["quantity"],
                asset["buy_price"]
            )

    except FileNotFoundError:
        pass
