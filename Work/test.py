class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # Check the call to `super` and `__init__`
      # super().__init__(name, shares, price)
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()
