from money import Money

class Portfolio:
    def __init__(self):
        self._exchange_rates = {
                "EUR->USD": 1.2,
                "USD->KRW": 1100
                }

    def add(self, *moneys):
        self.moneys = [ money for money in moneys ]

    def evaluate(self, bank, currency):
        sum = 0.0
        failures = []
        for money in self.moneys:
            try:
                sum += bank.convert(money, currency).amount
            except Exception as ex:
                failures.append(ex)
        if failures:
            failure_message = ", ".join(f.args[0] for f in failures)
            raise Exception("Missing exchange rate(s):[" + failure_message + "]")
        else:
            return Money(sum, currency)
