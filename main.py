from metatrader.metatrader import send_order, OrderRequest
from metatrader.market_data import tradeable_symbols


def main():
    tardeable = tradeable_symbols()
    # print(tardeable[0])

    symbol = "EURUSDm"

    buy_order = OrderRequest(
        symbol=symbol,
        volume=0.1,
        order_type="SELL",
        sl_points=100,
        tp_points=200,
        comment="Python SELL order",
    )

    result = send_order(buy_order)
    print("SELL Order Result:")
    print(result)


if __name__ == "__main__":
    main()
