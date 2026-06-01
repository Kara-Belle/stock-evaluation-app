import json

from data_fetcher import get_stock_data
from indicators import add_indicators
from strategy import get_signal
from portfolio import allocate_money

with open("config.json", "r") as file:
    config = json.load(file)

tickers = config["tickers"]
period = config["period"]

results = []

for ticker in tickers:

    data = get_stock_data(ticker, period)
    data = add_indicators(data)

    signal, score = get_signal(data)

    latest = data.iloc[-1]

    results.append({
        "ticker": ticker,
        "price": latest["Close"],
        "signal": signal,
        "score": score
    })

results.sort(
    key=lambda stock: stock["score"],
    reverse=True
)

print("\n=== STOCK RANKINGS ===\n")

for stock in results:

    print(
        f"{stock['ticker']:5} | "
        f"Score: {stock['score']} | "
        f"Signal: {stock['signal']} | "
        f"Price: ${stock['price']:.2f}"
    )

starting_money = config["starting_money"]

portfolio = allocate_money(results, starting_money)

print("\n=== PORTFOLIO ALLOCATION ===\n")
print(f"Starting Money: ${starting_money:,.2f}\n")

for stock in portfolio:
    print(
        f"{stock['ticker']:5} | "
        f"Shares: {stock['shares']} | "
        f"Spent: ${stock['amount_spent']:,.2f} | "
        f"Cash Left: ${stock['cash_left']:.2f}"
    )