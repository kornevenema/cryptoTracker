from pycoingecko import CoinGeckoAPI


# class to get crypto data from the API
class Getter:
    def __init__(self):
        self.currency = ' eur'
        self.cg = CoinGeckoAPI()

    def get_currency(self):
        return self.currency

    def set_currency(self, currency):
        self.currency = currency

    def get_curr_price(self, coin):
        return self.cg.get_price(ids=coin, vs_currencies=self.currency)

