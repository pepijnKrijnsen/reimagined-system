const Money = require("./money")

class Portfolio {
  constructor() {
    this.moneys = []
  }

  add(...moneys) {
    this.moneys = this.moneys.concat(moneys);
  }

  evaluate(currency) {
    let missing = [];
    let total = this.moneys.reduce((sum, money) => {
      let convertedAmount = this.convert(money, currency);
      if (!convertedAmount) {
        missing.push(money.currency + "->" + currency);
        return sum;
      }
      return sum + convertedAmount;
    }, 0);
    if (missing.length) {
      throw new Error("Missing exchange rate(s): [" + missing.join() + "]");
    } else {  // else is required here because we don't want to return
      return new Money(total, currency);  // a Money in case of errors
    }
  }

  convert(money, currency) {
    let exchangeRates = new Map();
    exchangeRates.set("EUR->USD", 1.2);
    exchangeRates.set("USD->KRW", 1100);
    if (money.currency === currency) {
      return money.amount;
    } else {
      let key = money.currency + "->" + currency;
      let rate = exchangeRates.get(key);
      if (rate) {
        return money.amount * rate;
      } else {
        return undefined;
      }
    }
  }
}

module.exports = Portfolio;
