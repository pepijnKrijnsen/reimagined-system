from money import Money

class Portfolio:
    def __init__(self):
        self._exchange_rates = {
                "EUR->USD": 1.2,
                "USD->KRW": 1100
                }

    def add(self, *moneys):
        self.moneys = [ money for money in moneys ]

    def evaluate(self, currency):
        sum = 0
        for money in self.moneys:
            if currency == money.currency:
                sum += money.amount
            else:
                sum += self._convert(money, currency)
        return Money(sum, currency)

    def _convert(self, money, currency):
        key = money.currency + "->" + currency
        return money.amount * self._exchange_rates[key]
