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
    executor.map(run_script, scripts)
