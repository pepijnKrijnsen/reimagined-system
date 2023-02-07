from money import Money

class Bank:
    def __init__(self) -> None:
        self.exchange_rates = {}

    def addExchangeRate(self, currency_from:str, currency_to:str, rate:float) -> None:
        key = currency_from + "->" + currency_to
        self.exchange_rates[key] = rate

    def convert(self, a_money:object, a_currency:str) -> object:
        if a_money.currency == a_currency:
            return Money(a_money.amount, a_currency)
        key = a_money.currency + "->" + a_currency
        if key in self.exchange_rates:
            return Money(a_money.amount * self.exchange_rates[key],
                         a_currency)
        else:
            raise Exception(key)
