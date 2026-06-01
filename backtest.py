from data_fetcher import get_stock_data
from indicators import add_indicators


def run_backtest(ticker, period, starting_money):
    data = get_stock_data(ticker, period)
    data = add_indicators(data)

    start_price = data["Close"].iloc[0]
    end_price = data["Close"].iloc[-1]

    shares = starting_money / start_price
    final_value = shares * end_price

    return {
        "ticker": ticker,
        "start_price": start_price,
        "end_price": end_price,
        "starting_money": starting_money,
        "final_value": final_value,
        "profit": final_value - starting_money
    }