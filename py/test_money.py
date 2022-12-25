from logging import currentframe
import unittest

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)


class Portfolio:
    def __init__(self):
        self.sum = 0

    def add(self, *moneys):
        for money in moneys:
            self.sum += money.amount

    def evaluate(self, currency):
        return Money(self.sum, currency)


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollar(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        self.assertEqual(fiveDollars.times(2), tenDollars)

    def testMultiplicationInEuro(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")
        self.assertEqual(tenEuros.times(2), twentyEuros)

    def testDivision(self):
        original_money = Money(4002, "KRW")
        actual_money_after_division = original_money.divide(4)
        expected_money_after_division = Money(1000.5, "KRW")
        self.assertEqual(actual_money_after_division,
                         expected_money_after_division)

    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))


if __name__ == "__main__":
    unittest.main()
