import os
import threading, back

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
# riordino i simboli in ordine alfabetico
symbols.sort()

timeframes = ['15M', '30M', '1H', '4H', '1D']


def loop_genera_csv():
    while True:
        for timeframe in timeframes:
            for symbol in symbols:
                print(f"Aggiorno {symbol} {timeframe}")
                back.genera_csv(symbol, timeframe)


def loop_esegui_calcoli():
    os.system(f"streamlit run front.py")


# Creiamo due thread separati per eseguire le funzioni in parallelo
thread_genera_csv = threading.Thread(target=loop_genera_csv)
thread_esegui_calcoli = threading.Thread(target=loop_esegui_calcoli)

# Avviamo i thread
thread_genera_csv.start()
thread_esegui_calcoli.start()

# Attendiamo che i thread terminino (questo non accadrà mai)
thread_genera_csv.join()
thread_esegui_calcoli.join()

os.system(f"streamlit run front.py --browser.gatherUsageStats False")

thread_genera_csv.join()
thread_esegui_calcoli.join()
