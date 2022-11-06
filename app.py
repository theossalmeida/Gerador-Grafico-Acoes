import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import design
from backend import puxa_dados, normalizacao
from pyqtgraph import PlotWidget, plot
import pandas as pd
from pandas_datareader import data as wb
import matplotlib as plt
import numpy as np


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
            return data_usuario_final

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
        self.grafico.show(
            puxa_dados(acoes, data_usuario_inicio[len(data_usuario_inicio)-1], 
            data_usuario_final[len(data_usuario_final)-1])
        )

    def normaliza(self):
        self.grafico.show(
            normalizacao(acoes, data_usuario_inicio[len(data_usuario_inicio)-1], 
            data_usuario_final[len(data_usuario_final)-1])
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    GeraGrafico = GeraGrafico()
    GeraGrafico.show()
    qt.exec_()
