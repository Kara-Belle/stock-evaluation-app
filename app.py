import json

from data_fetcher import get_stock_data
from indicators import add_indicators
from strategy import get_signal
from portfolio import calculate_portfolio

with open("config.json", "r") as file:
    config = json.load(file)

ticker = config["tickers"][0]
period = config["period"]
starting_money = config["starting_money"]

data = get_stock_data(ticker, period)
data = add_indicators(data)

signal = get_signal(data)
latest = data.iloc[-1]

shares, cash = calculate_portfolio(starting_money, latest["Close"])

print("\nStock:", ticker)
print(f"Current Price: ${latest['Close']:.2f}")
print(f"50 Day Average: ${latest['MA50']:.2f}")
print(f"200 Day Average: ${latest['MA200']:.2f}")
print(f"Signal: {signal}")

print(f"\nStarting Money: ${starting_money:,.2f}")
print(f"Shares Purchased: {shares}")
print(f"Cash Remaining: ${cash:.2f}")