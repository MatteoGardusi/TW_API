import os

os.system("pip install pandas_ta")
os.system("python.exe -m pip install --upgrade pip")
os.system("pip install streamlit_autorefresh")
os.system("pip install pandas_ta")
os.system("pip uninstall websocket")
os.system("pip install websocket-client==0.44.0")
# installiamo i requirements.txt
os.system("pip install -r requirements.txt")

symbols = ['EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'AUDUSD', 'USDCAD', 'NZDUSD', 'EURGBP', 'EURJPY', 'EURCHF', 'EURAUD',
           'AUDCAD', 'AUDJPY', 'AUDNZD', 'CADJPY', 'NZDCAD', 'NZDCHF', 'NZDJPY', 'CHFJPY', 'CADCHF',
           'EURCAD', 'AUDCHF', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPNZD', 'GBPJPY', 'EURNZD', ]

timeframes = ['15M', '30M', '1H', '4H', '1D']

import threading, back


def loop_genera_csv():
    while True:
        for timeframe in timeframes:
            for symbol in symbols:
                print(f"Aggiorno {symbol} {timeframe}")
                back.genera_csv(symbol, timeframe)


thread_genera_csv = threading.Thread(target=loop_genera_csv)

thread_genera_csv.start()

os.system(f"streamlit run front.py --browser.gatherUsageStats False --no-warn-script-location")

thread_genera_csv.join()
