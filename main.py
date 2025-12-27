import MetaTrader5 as mt5
from metatrader.metatrader import close_order


def main():
    d = close_order(961882140, comment="Test close order")
    print(d)


if __name__ == "__main__":
    main()
