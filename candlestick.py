import pandas as pd
import talib
import mplfinance as fplt
import streamlit as st
import altair as alt
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("RSI Strategy by Teo")

symbols = ['EURUSD', 'GBPUSD', 'USDJPY', 'USDCHF', 'AUDUSD', 'USDCAD', 'NZDUSD', 'EURGBP', 'EURJPY', 'EURCHF', 'EURAUD',
           'AUDCAD', 'AUDJPY', 'AUDNZD', 'CADJPY', 'NZDCAD', 'NZDCHF', 'NZDJPY', 'CHFJPY', 'CADCHF',
           'EURCAD', 'AUDCHF', 'GBPAUD', 'GBPCAD', 'GBPCHF', 'GBPNZD', 'GBPJPY', 'EURNZD', ]

tf = st.sidebar.selectbox("Select Timeframe", ["15M", "30M", "1H", "4H", "1D"])
df = pd.read_csv(f'data/EURUSD/{tf}/EURUSD_{tf}.csv', parse_dates=True)
df.datetime = pd.to_datetime(df.datetime)


def plot(symbol, tf):
    df = pd.read_csv(f'data/{symbol}/{tf}/{symbol}_{tf}.csv', parse_dates=True)
    df.datetime = pd.to_datetime(df.datetime)
    # Crea il grafico candlestick
    fig = go.Figure(data=[go.Candlestick(x=df["datetime"],
                                         open=df["open"],
                                         high=df["high"],
                                         low=df["low"],
                                         close=df["close"],
                                         name=f"{symbol}")])

    # Aggiungi il grafico RSI come secondario
    fig.add_trace(
        go.Scatter(x=df["datetime"], y=df["RSI"], mode="lines", name="RSI", yaxis="y2", line=dict(color='white')))

    # Configura l'asse y2 per il grafico RSI
    fig.update_layout(yaxis2=dict(anchor="x", overlaying="y", side="right"))

    # Aggiungi titoli e label
    fig.update_layout(title=f"{symbol}",
                      xaxis_title="Data",
                      yaxis_title="Prezzo",
                      yaxis2_title="RSI")

    # Nascondi la barra di navigazione (zoom)
    fig.update_layout(xaxis=dict(rangeslider=dict(visible=False)))

    st.plotly_chart(fig)


col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

with col1:
    for symbol in symbols[:4]:
        plot(symbol, tf)
with col2:
    for symbol in symbols[4:8]:
        plot(symbol, tf)
with col3:
    for symbol in symbols[8:12]:
        plot(symbol, tf)
with col4:
    for symbol in symbols[12:16]:
        plot(symbol, tf)
with col5:
    for symbol in symbols[16:20]:
        plot(symbol, tf)
with col6:
    for symbol in symbols[20:24]:
        plot(symbol, tf)
with col7:
    for symbol in symbols[24:]:
        plot(symbol, tf)
