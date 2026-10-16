from portfolio import Portfolio



def test_add():

    p = Portfolio()

    p.add_asset(
        "AAPL",
        5,
        180
    )

    assert len(p.assets)==1



def test_invested():

    p = Portfolio()

    p.add_asset(
        "BTC",
        2,
        50000
    )


    assert p.total_invested()==100000



def test_profit():

    p = Portfolio()

    p.add_asset(
        "BTC",
        1,
        50000
    )


    prices={
        "BTC":60000
    }


    assert p.total_profit(prices)==10000
