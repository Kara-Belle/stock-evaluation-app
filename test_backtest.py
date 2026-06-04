from backtest import run_backtest

starting_money = 10000
period = "5y"

stock_result = run_backtest(
    ticker="AAPL",
    period=period,
    starting_money=starting_money
)

market_result = run_backtest(
    ticker="SPY",
    period=period,
    starting_money=starting_money
)

print("\n=== BACKTEST COMPARISON ===\n")

print(f"Stock: {stock_result['ticker']}")
print(f"Final Value: ${stock_result['final_value']:,.2f}")
print(f"Profit: ${stock_result['profit']:,.2f}")

print("\nMarket Benchmark: SPY")
print(f"Final Value: ${market_result['final_value']:,.2f}")
print(f"Profit: ${market_result['profit']:,.2f}")

difference = stock_result["final_value"] - market_result["final_value"]

print("\n=== RESULT ===")

if difference > 0:
    print(f"{stock_result['ticker']} beat SPY by ${difference:,.2f}")
else:
    print(f"{stock_result['ticker']} lost to SPY by ${abs(difference):,.2f}")