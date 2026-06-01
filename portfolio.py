def calculate_portfolio(starting_money, stock_price):

    shares = int(starting_money // stock_price)

    cash_left = starting_money - (shares * stock_price)

    return shares, cash_left