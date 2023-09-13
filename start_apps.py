import concurrent.futures
import os


# Funzione per eseguire uno script
def run_script(script_name):
    if script_name == "main.py":
        os.system(f"python {script_name}")
    elif script_name == "app.py":
        os.system(f"streamlit run {script_name}")


# Nomi degli script da eseguire
scripts = ["main.py", "app.py"]

# Usa ThreadPoolExecutor per eseguire gli script contemporaneamente
with concurrent.futures.ThreadPoolExecutor() as executor:
    # installo la wheel di talib
    os.system("pip install ta_lib-0.4.25-cp311-cp311-win_amd64.whl")
    os.system("pip install streamlit_autorefresh")
    executor.map(run_script, scripts)
