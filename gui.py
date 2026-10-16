import tkinter as tk
from tkinter import messagebox

from portfolio import Portfolio
from database import save_portfolio
from market import get_price
from charts import show_chart



portfolio = Portfolio()



def refresh():

    text.delete("1.0", tk.END)

    prices = {}


    for asset in portfolio.assets:

        prices[asset.symbol] = get_price(asset.symbol)


    value = portfolio.total_value(prices)

    profit = portfolio.total_profit(prices)


    text.insert(
        tk.END,
        f"Portfolio value : ${value:.2f}\n"
    )

    text.insert(
        tk.END,
        f"Profit : ${profit:.2f}\n\n"
    )


    for asset in portfolio.assets:

        text.insert(
            tk.END,
            f"{asset.symbol} "
            f"{asset.quantity} units\n"
        )



def add():

    symbol = entry_symbol.get().upper()

    quantity = float(entry_quantity.get())

    price = float(entry_price.get())


    portfolio.add_asset(
        symbol,
        quantity,
        price
    )


    save_portfolio(portfolio)

    refresh()



def remove():

    symbol = entry_symbol.get().upper()

    portfolio.remove_asset(symbol)

    save_portfolio(portfolio)

    refresh()



window = tk.Tk()

window.title(
    "Portfolio Tracker"
)

window.geometry(
    "500x500"
)



tk.Label(
    window,
    text="Portfolio Tracker",
    font=("Arial",20)
).pack()



entry_symbol = tk.Entry(window)

entry_symbol.pack()

entry_symbol.insert(
    0,
    "Symbol"
)



entry_quantity = tk.Entry(window)

entry_quantity.pack()

entry_quantity.insert(
    0,
    "Quantity"
)



entry_price = tk.Entry(window)

entry_price.pack()

entry_price.insert(
    0,
    "Buy price"
)



tk.Button(
    window,
    text="Add",
    command=add
).pack()



tk.Button(
    window,
    text="Remove",
    command=remove
).pack()



tk.Button(
    window,
    text="Refresh",
    command=refresh
).pack()



text = tk.Text(
    window,
    height=15,
    width=50
)

text.pack()



window.mainloop()
