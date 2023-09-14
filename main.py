import pandas as pd
import pandas_ta as pta
import tvDatafeed
from tvDatafeed import TvDatafeedLive
import os

tv = TvDatafeedLive()

symbols = ['EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'AUDUSD', 'USDCAD', 'NZDUSD', 'EURGBP', 'EURJPY', 'EURCHF', 'EURAUD',
           'AUDCAD', 'AUDJPY', 'AUDNZD', 'CADJPY', 'NZDCAD', 'NZDCHF', 'NZDJPY', 'CHFJPY', 'CADCHF',
           'EURCAD', 'AUDCHF', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPNZD', 'GBPJPY', 'EURNZD', ]

timeframes = ['15M', '30M', '1H', '4H', '1D']


def genera_csv(symbol, timeframe):
    if timeframe == '15M':
        data = tv.get_hist(f"{symbol}", "OANDA", interval=tvDatafeed.Interval.in_15_minute, n_bars=500,
                           fut_contract=None,
                           extended_session=False, timeout=-1)
    elif timeframe == '30M':
        data = tv.get_hist(f"{symbol}", "OANDA", interval=tvDatafeed.Interval.in_30_minute, n_bars=500,
                           fut_contract=None,
                           extended_session=False, timeout=-1)
    elif timeframe == '1H':
        data = tv.get_hist(f"{symbol}", "OANDA", interval=tvDatafeed.Interval.in_1_hour, n_bars=500, fut_contract=None,
                           extended_session=False, timeout=-1)
    elif timeframe == '4H':
        data = tv.get_hist(f"{symbol}", "OANDA", interval=tvDatafeed.Interval.in_4_hour, n_bars=500, fut_contract=None,
                           extended_session=False, timeout=-1)
    elif timeframe == '1D':
        data = tv.get_hist(f"{symbol}", "OANDA", interval=tvDatafeed.Interval.in_daily, n_bars=500, fut_contract=None,
                           extended_session=False, timeout=-1)

    data.drop(columns='volume', inplace=True)
    data["RSI"] = pta.rsi(data['close'], length=14)
    # Ecco un esempio di come farlo:
    df1 = pd.DataFrame(pd.to_datetime(data.index))
    df2 = pd.DataFrame(data)
    df2.reset_index(drop=True, inplace=True)
    # Concatena le due colonne in un unico DataFrame
    df = pd.concat([df1, df2], axis=1)
    df = df.dropna(subset=['RSI'])
    df.reset_index(drop=True, inplace=True)
    if not os.path.exists(f"data/{symbol}"):
        os.makedirs(f"data/{symbol}")
    if not os.path.exists(f"data/{symbol}/{timeframe}"):
        os.makedirs(f"data/{symbol}/{timeframe}")

    df.to_csv(f"data/{symbol}/{timeframe}/{symbol}_{timeframe}.csv", index=False)


while True:

    for timeframe in timeframes:
        for symbol in symbols:
            print(f"Aggiorno {symbol} {timeframe}")
            genera_csv(symbol, timeframe)
