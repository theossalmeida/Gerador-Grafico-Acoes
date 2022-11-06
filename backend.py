import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import numpy as np
# import yfinance as yfin
# yfin.pdr_override()


dados = pd.DataFrame()


def puxa_dados(lista, data_inicio, data_final):
    for i in lista:
        dados[i] = wb.get_data_yahoo(i, start=data_inicio, end=data_final)[
            'Adj Close']

    dados.plot(figsize=(15, 6))
    plt.show()


def normalizacao(lista, data_inicio, data_final):
    for i in lista:
        dados[i] = wb.get_data_yahoo(i, start=data_inicio, end=data_final)[
            'Adj Close']

    (dados / dados.iloc[0]).plot(figsize=(15, 6))
    plt.show()


