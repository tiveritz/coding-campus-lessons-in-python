def currency_calculator():
    print(get_converted_currency(100, "EUR"))
    print(get_converted_currency(100, "USD"))
    print(get_converted_currency(100, "CHF"))
    print(get_converted_currency(100, "SEK"))
    print(get_converted_currency(100, "ASDF"))
    print(get_converted_currency(100, 1.23))

def get_converted_currency(amount, rate):
    # Generally it isn't a good idea that a function can return different types...
    exchange_rates = {
        "CHF" : 1.07,
        "USD" : 1.18,
        "SEK" : 10.35
    }

    if rate in exchange_rates:
        return exchange_rates[rate] * amount
    elif type(rate) == str:
        return "Unknown currency"
    else:
        return amount * rate
