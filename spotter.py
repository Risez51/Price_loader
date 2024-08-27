class Spotter:
    def __init__(self):
        self.nds = 1.2

    def get_balance_adjustment_stock(self, stock):
        if self.get_type_stock(stock) >= 1000000:
            return 100000
        else:
            return stock

    def get_type_stock(self, stock):
        if isinstance(float(stock), float):
            return int(float(stock))
        elif isinstance(int(stock), int):
            return int(stock)
        else:
            return 0
