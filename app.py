import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import design
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

dados = pd.DataFrame()
acoes = []
data_usuario_inicio = []
data_usuario_final = []
acao = ""


class GeraGrafico(QMainWindow, design.Ui_displayGrafico):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.addDataInicial.clicked.connect(self.add_data_inicio)
        self.addDataFinal.clicked.connect(self.add_data_final)
        self.addLista.clicked.connect(self.add_lista)
        self.limpaLista.clicked.connect(self.limpa_lista)
        self.geraGrafico.clicked.connect(self.gera_grafico)
        self.Normalizar.clicked.connect(self.normaliza)

    def add_data_inicio(self):
        data_usuario_inicio.append(self.recebeDataInicio.text())
        return data_usuario_inicio

    def add_data_final(self):
        data_usuario_final.append(self.recebeDataFinal.text())
        return str(data_usuario_final)

    def add_lista(self):
        acao = self.recebeAcao.text()
        acoes.append(str(acao))
        self.displayLista.setText(
            str(acoes)
        )
        return acoes

    def limpa_lista(self):
        acoes.clear()
        self.displayLista.setText(
            str(acoes)
        )

    def gera_grafico(self):
        self.figure.clear()
        if len(data_usuario_final) != 0:
            for i in acoes:
                dados[i] = wb.DataReader(i, data_source="yahoo", start=data_usuario_inicio[len(data_usuario_inicio)-1],
                                         end=data_usuario_final[len(data_usuario_final)-1])['Adj Close']
        else:
            for i in acoes:
                dados[i] = wb.DataReader(i, data_source="yahoo", start=data_usuario_inicio[len(
                    data_usuario_inicio)-1])['Adj Close']

        plt.plot(dados)
        plt.legend(dados)
        self.canvas.draw()

    def normaliza(self):
        self.figure.clear()
        if len(data_usuario_final) != 0:
            for i in acoes:
                dados[i] = wb.DataReader(i, data_source="yahoo", start=data_usuario_inicio[len(data_usuario_inicio)-1],
                                         end=data_usuario_final[len(data_usuario_final)-1])['Adj Close']
        else:
            for i in acoes:
                dados[i] = wb.DataReader(i, data_source="yahoo", start=data_usuario_inicio[len(
                    data_usuario_inicio)-1])['Adj Close']

        plt.plot((dados / dados.iloc[0]))
        plt.legend(dados)
        self.canvas.draw()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    GeraGrafico = GeraGrafico()
    GeraGrafico.show()
    qt.exec_()
