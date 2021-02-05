from tracker import common, getter


class Data:
    def __init__(self):
        self.getter = getter.Getter()
        self.all_coins = common.get_all_coins()



