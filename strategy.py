def get_signal(data):

    latest = data.iloc[-1]

    price = latest["Close"]
    ma50 = latest["MA50"]
    ma200 = latest["MA200"]

    score = 0

    if price > ma50:
        score += 1

    if ma50 > ma200:
        score += 1

    if price > ma200:
        score += 1

    if score == 3:
        signal = "BUY"
    elif score == 2:
        signal = "HOLD"
    else:
        signal = "SELL"

    return signal, score