def allocate_money(results, starting_money):
    buy_stocks = [stock for stock in results if stock["signal"] == "BUY"]

    if len(buy_stocks) == 0:
        return []

    money_per_stock = starting_money / len(buy_stocks)

    portfolio = []

    for stock in buy_stocks:
        shares = int(money_per_stock // stock["price"])
        amount_spent = shares * stock["price"]
        cash_left = money_per_stock - amount_spent

        portfolio.append({
            "ticker": stock["ticker"],
            "price": stock["price"],
            "shares": shares,
            "amount_spent": amount_spent,
            "cash_left": cash_left
        })

    return portfolio