import os


# Funzione per eseguire uno script
def run_script(script_name):
    if script_name == "back.py":
        os.system(f"python {script_name}")
    elif script_name == "front.py":
        os.system(f"streamlit run {script_name}")


# Nomi degli script da eseguire
scripts = ["back.py", "front.py"]
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

os.system(f"streamlit run front.py --server.gatherUsageStats False")
