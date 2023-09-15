import pandas as pd
import streamlit as st
from streamlit_autorefresh import st_autorefresh
import time
import plotly.graph_objects as go

st.set_page_config(page_title="RSI Strategy by Teo", page_icon="📊", layout="wide")
st.subheader("RSI Strategy by Teo")


symbols = ['EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'AUDUSD', 'USDCAD', 'NZDUSD', 'EURGBP', 'EURJPY', 'EURCHF', 'EURAUD',
           'AUDCAD', 'AUDJPY', 'AUDNZD', 'CADJPY', 'NZDCAD', 'NZDCHF', 'NZDJPY', 'CHFJPY', 'CADCHF',
           'EURCAD', 'AUDCHF', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPNZD', 'GBPJPY', 'EURNZD', ]


def esegui_calcoli():
    df = pd.read_csv(f'data/EURUSD/15M/EURUSD_15M.csv', parse_dates=True)

    last_update = df['datetime'].iloc[-1]
    st.write(f"Last Update: {last_update}")

    def plot(symbol, tf):
        df = pd.read_csv(f'data/{symbol}/{tf}/{symbol}_{tf}.csv', parse_dates=True)

        df.datetime = pd.to_datetime(df.datetime)
        # Crea il grafico candlestick
        # Crea il grafico dell'RSI con Plotly
        fig = go.Figure(data=[go.Scatter(x=df['datetime'], y=df['RSI'], mode='lines')])
        fig.update_layout(
            title=f"{symbol}",
            xaxis_title="Data",
            yaxis_title="RSI",
            # aggiungo una scritta cons scritto ciao in basso a destra del grafico
        )
        # aggiungo la linea di 30 e 70 colore bianco
        fig.add_shape(
            type="line",
            x0=df['datetime'].iloc[0],
            y0=30,
            x1=df['datetime'].iloc[-1],
            y1=30,
            line=dict(
                color="white",
                width=1,
                dash="dashdot",
            ),
        )
        fig.add_shape(
            type="line",
            x0=df['datetime'].iloc[0],
            y0=70,
            x1=df['datetime'].iloc[-1],
            y1=70,
            line=dict(
                color="white",
                width=1,
                dash="dashdot",
            ),
        )
        # voglio costruire una logica che mi restituisce se l'ultima volta l'RSI è stato sotto 30 o sopra 70
        # se l'ultima volta è stato sotto 30 e ora è sopra 30 allora è un segnale di vendita
        # se l'ultima volta è stato sopra 70 e ora è sotto 70 allora è un segnale di acquisto
        var = 0
        for row in df.index:
            if df['RSI'][row] < 30:
                var = 'SELL'
            elif df['RSI'][row] > 70:
                var = 'BUY'
        if tf == "15M":
            if var == 'SELL' and df['RSI'][len(df) - 1] <= 35:
                var = 'SELL ⚠️'
            elif var == 'BUY' and df['RSI'][len(df) - 1] >= 65:
                var = 'BUY ⚠️'
        return var

    def fun_col(symbol):
        list = [symbol]
        for tf in ['15M', '30M', '1H', '4H', '1D']:
            list.append(plot(symbol, tf))
        # creo una tabella che ha come prima riga il primo elmento della lista e successivamente tutte le altre righe
        # faccio in modo che la tabella abbia la cella con sfondo rosso se il valore è SELL e verde se è BUY

        # Crea un DataFrame con i dati
        return list

    def color_df(df):
        # Funzione per colorare le celle
        def highlight_cells(val):
            if val == "BUY":
                color = "background-color: green"
            elif val == "SELL":
                color = "background-color: red"
            elif val == "BUY ⚠️" or val == "SELL ⚠️":
                color = "background-color: yellow"
            else:
                # il colore rimane trasparente
                color = "background-color: transparent"
            return color

        # Applica la formattazione alle celle
        styled_df = df.style.applymap(highlight_cells)
        # nascondo gli indici delle righe e delle colonne

        # Visualizza il DataFrame con le celle colorate
        return styled_df

    list_df = []
    for symbol in symbols:
        list_df.append(fun_col(symbol))

    def get_order_type(data):
        # conto il numero di BUY e BUY ⚠️
        buy_count = data.count("BUY") + data.count("BUY ⚠️")
        # conto il numero di SELL e SELL ⚠️
        sell_count = data.count("SELL") + data.count("SELL ⚠️")

        if buy_count == 5:
            return 0, -sell_count
        elif sell_count == 5:
            return (1, -buy_count)
        else:
            return (2, 0)

    # Ordina la lista utilizzando la funzione di ordinamento personalizzata
    sorted_data_list = sorted(list_df, key=get_order_type)

    list_df = []
    for data in sorted_data_list:
        list_df.append(pd.DataFrame(data))

    list_df_col = []
    for df in list_df:
        list_df_col.append(color_df(df))

    # Numero di colonne per riga
    num_cols = 7

    # Calcola il numero di righe necessarie
    num_rows = -(-len(list_df_col) // num_cols)  # Divisione intera arrotondata per eccesso

    # Crea una struttura di loop annidati per organizzare i DataFrame per righe
    for row in range(num_rows):
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

        for i in range(num_cols):
            index = row * num_cols + i
            if index < len(list_df_col):
                with col1 if i == 0 else col2 if i == 1 else col3 if i == 2 else col4 if i == 3 else col5 if i == 4 else col6 if i == 5 else col7:
                    st.dataframe(list_df_col[index], use_container_width=True)


count = st_autorefresh(interval=30000)
if count != 0:
    esegui_calcoli()
