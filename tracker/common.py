from json import load


# get coins from coins.json
def get_coins():
    with open('coins.json', 'r') as f:
        return load(f)


# get all coins from all_coins.json
def get_all_coins():
    with open('all_coins.json', 'r') as f:
        return load(f)

