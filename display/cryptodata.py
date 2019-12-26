from pycoingecko import CoinGeckoAPI

class CryptoData:
    def __init__(self):
        self.cg = CoinGeckoAPI()

    def get_currencies(self):
        return self.cg.get_coins_markets(vs_currency='usd')
