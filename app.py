import concurrent.futures
import os


# Funzione per eseguire uno script
def run_script(script_name):
    if script_name == "back.py":
        os.system(f"python {script_name}")
    elif script_name == "front.py":
        os.system(f"streamlit run {script_name}")


# Nomi degli script da eseguire
scripts = ["back.py", "front.py"]

# Usa ThreadPoolExecutor per eseguire gli script contemporaneamente
with concurrent.futures.ThreadPoolExecutor() as executor:
    # installo la wheel di talib
    os.system("pip install streamlit_autorefresh")
    os.system("pip install pandas_ta")
    executor.map(run_script, scripts)
