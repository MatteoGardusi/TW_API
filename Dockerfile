
# Usa' unimmagine di base che include Python (puoi specificare la versione desiderata)
FROM python:3.11

# Crea una directory di lavoro all'interno del contenitore
WORKDIR /TW_API

# Copia il tuo file app.py nella directory di lavoro del contenitore
COPY app.py .

# Crea un ambiente virtuale
RUN python -m venv venv

# Attiva l'ambiente virtuale
SHELL ["/bin/bash", "-c"]
RUN source venv/bin/activate

# Installa le dipendenze del tuo script all'interno dell'ambiente virtuale
COPY requirements.txt .
RUN pip install -r requirements.txt

# Specifica il comando per eseguire il tuo script all'interno dell'ambiente virtuale quando il contenitore viene avviato
CMD ["python", "app.py"]

# Esponi la porta TCP
EXPOSE 8000
