import json
import requests
from config import keys


class ConverthionExeption(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise ConverthionExeption(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            qoute_ticker = keys[quote]
        except KeyError:
            raise ConverthionExeption(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConverthionExeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConverthionExeption(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={qoute_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]
        total_base = round(abs(float(amount)) * float(total_base), 4)
        return total_base
