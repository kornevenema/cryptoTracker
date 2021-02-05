from tracker import common, data, getter
from json import dump


def check_coin(coin):
    coin = coin.lower()
    all_coins = common.get_all_coins()
    if coin in all_coins:
        return True
    else:
        return False


def add_coin(coin):
    coin = coin.lower()
    if check_coin(coin):
        all_coins = common.get_all_coins()
        coins = common.get_coins()
        coins[coin] = all_coins[coin]
        with open('coins.json', 'w') as f:
            dump(coins, f, indent=4)
        return True
    else:
        return False


class Tracker:
    def __init__(self):
        self.coins = common.get_coins()
        self.getter = getter.Getter()
        self.data = data.Data()

    def add_coin(self, coin):
        if add_coin(coin):
            print(coin, 'added')
            self.coins = common.get_coins()
        else:
            print(coin, "couldn't be added.")

