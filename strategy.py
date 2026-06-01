def get_signal(data):

    latest = data.iloc[-1]

    price = latest["Close"]
    ma50 = latest["MA50"]
    ma200 = latest["MA200"]

    if price > ma50 and ma50 > ma200:
        return "BUY"

    elif price < ma50:
        return "SELL"

    else:
        return "HOLD"