from backtest import run_backtest

result = run_backtest(
    ticker="AAPL",
    period="5y",
    starting_money=10000
)

print("\n=== BACKTEST ===\n")
print(f"Ticker: {result['ticker']}")
print(f"Start Price: ${result['start_price']:.2f}")
print(f"End Price: ${result['end_price']:.2f}")
print(f"Starting Money: ${result['starting_money']:,.2f}")
print(f"Final Value: ${result['final_value']:,.2f}")
print(f"Profit: ${result['profit']:,.2f}")