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
        failures = []
        for money in self.moneys:
            if currency == money.currency:
                sum += money.amount
            else:
                try:
                    sum += self._convert(money, currency)
                except KeyError as ke:
                    failures.append(ke)
        if failures:
            failure_message = ", ".join(f.args[0] for f in failures)
            raise Exception("Missing exchange rate(s):[" + failure_message + "]")
        else:
            return Money(sum, currency)

    def _convert(self, money, currency):
        key = money.currency + "->" + currency
        return money.amount * self._exchange_rates[key]
