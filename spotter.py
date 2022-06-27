class Spotter:
    def __init__(self):
        self.nds = 1.2

    def get_balance_adjustment_stock(self, stock):
        if int(stock) >= 1000000:
            return 100000
        else:
            return stock