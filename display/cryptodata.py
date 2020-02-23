from pycoingecko import CoinGeckoAPI

class CryptoData:
    def __init__(self):
        self.cg = CoinGeckoAPI()
        self.currencies = self.cg.get_coins_markets(vs_currency='usd')

    def get_currencies(self):
        return self.currencies


    def get_history(self, coin):
        return self.cg.get_coin_history_by_id(id=coin, date='30-12-2017')


    def get_coin_info(self,coin):
        return self.cg.get_coin_by_id(coin)

    def get_coin_price(self, coin):
        return self.cg.get_price(id=coin, vs_currency='usd')
