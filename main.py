from metatrader.market_data import candle_data, symbol_info, tradeable_symbols
import MetaTrader5 as mt5


def main():
    data = candle_data("EURUSDm", mt5.TIMEFRAME_M1, 0, 100)

    one_min = mt5.TIMEFRAME_M1
    five_min = mt5.TIMEFRAME_M5
    fifteen_min = mt5.TIMEFRAME_M15
    thirty_min = mt5.TIMEFRAME_M30
    one_hour = mt5.TIMEFRAME_H1
    four_hour = mt5.TIMEFRAME_H4
    one_day = mt5.TIMEFRAME_D1
    one_week = mt5.TIMEFRAME_W1
    one_month = mt5.TIMEFRAME_MN1
    print("Timeframes:")
    print(
        one_min,
        five_min,
        fifteen_min,
        thirty_min,
        one_hour,
        four_hour,
        one_day,
        one_week,
        one_month,
    )


if __name__ == "__main__":
    main()
