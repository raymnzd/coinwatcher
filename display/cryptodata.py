import json
import os

import redis
from pycoingecko import CoinGeckoAPI

_host = "redis" if os.environ.get("REDIS_CONTAINER") else "localhost"


class CryptoData:
    def __init__(self):
        self.cg = CoinGeckoAPI()
        self._redis_client = redis.Redis(host=_host, port=6379, db=0)

    def get_currencies(self):
        currencies = self._redis_client.get("currencies")
        if currencies:
            currencies = json.loads(currencies)
            return [currencies[x] for x in currencies]

        currencies = self.cg.get_coins_markets(vs_currency="usd")
        currencies_dict = {}
        for coin in currencies:
            currencies_dict[coin["id"]] = coin

        self._redis_client.set("currencies", json.dumps(currencies_dict))
        self._redis_client.expire("currencies", 300)
        return currencies

    def get_history(self, coin):
        return self.cg.get_coin_history_by_id(id=coin, date="30-12-2017")

    def get_coin_info(self, coin):
        info_key = f"{coin}_info"
        info = self._redis_client.get(info_key)
        if info:
            return json.loads(info)
        info = self.cg.get_coin_by_id(coin)
        self._redis_client.set(info_key, json.dumps(info))
        return info

    def get_coin_price(self, coin):
        price_key = f"{coin}_price"
        price = self._redis_client.get(price_key)
        if price:
            return json.loads(price)
        price = self.cg.get_price(ids=coin, vs_currencies="usd")
        self._redis_client.set(price_key, json.dumps(price))
        self._redis_client.expire(price_key, 300)
        return price
