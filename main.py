from tracker.getter import Getter


def main():
    getter = Getter()
    print(getter.get_coins())
    getter.add_coin('doge')
    print(getter.get_coins())


main()
