import json
from tracker.getter import Getter


def main():
    getter = Getter()
    all_coins = getter.get_all_coins()
    print(all_coins)
    coins = {}

    for item in all_coins:
        coins[item['symbol']] = item['id']

    with open('all_coins.json', 'w') as f:
        json.dump(coins, f, indent=4)


main()
