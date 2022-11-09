import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_displayGrafico(object):
    def setupUi(self, displayGrafico):
        displayGrafico.setObjectName("displayGrafico")
        displayGrafico.resize(1280, 695)
        displayGrafico.setMinimumSize(QtCore.QSize(372, 300))
        displayGrafico.setMaximumSize(QtCore.QSize(1280, 968))
        displayGrafico.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        displayGrafico.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        displayGrafico.setWindowIcon(icon)
        displayGrafico.setLayoutDirection(QtCore.Qt.LeftToRight)
        displayGrafico.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(displayGrafico)
        self.centralwidget.setObjectName("centralwidget")
        self.addLista = QtWidgets.QPushButton(self.centralwidget)
        self.addLista.setGeometry(QtCore.QRect(540, 10, 111, 41))
        self.addLista.setObjectName("addLista")
        self.limpaLista = QtWidgets.QPushButton(self.centralwidget)
        self.limpaLista.setGeometry(QtCore.QRect(540, 60, 111, 41))
        self.limpaLista.setObjectName("limpaLista")
        self.geraGrafico = QtWidgets.QPushButton(self.centralwidget)
        self.geraGrafico.setGeometry(QtCore.QRect(650, 110, 601, 61))
        self.geraGrafico.setObjectName("geraGrafico")
        self.Normalizar = QtWidgets.QPushButton(self.centralwidget)
        self.Normalizar.setGeometry(QtCore.QRect(10, 110, 641, 61))
        self.Normalizar.setObjectName("Normalizar")
        self.recebeAcao = QtWidgets.QLineEdit(self.centralwidget)
        self.recebeAcao.setGeometry(QtCore.QRect(20, 10, 511, 41))
        self.recebeAcao.setObjectName("recebeAcao")
        self.recebeDataInicio = QtWidgets.QLineEdit(self.centralwidget)
        self.recebeDataInicio.setGeometry(QtCore.QRect(660, 10, 461, 41))
        self.recebeDataInicio.setObjectName("recebeDataInicio")
        self.displayLista = QtWidgets.QLabel(self.centralwidget)
        self.displayLista.setGeometry(QtCore.QRect(20, 60, 511, 41))
        self.displayLista.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.displayLista.setText("")
        self.displayLista.setObjectName("displayLista")
        self.addDataInicial = QtWidgets.QPushButton(self.centralwidget)
        self.addDataInicial.setGeometry(QtCore.QRect(1140, 10, 111, 41))
        self.addDataInicial.setObjectName("addDataInicial")
        self.addDataFinal = QtWidgets.QPushButton(self.centralwidget)
        self.addDataFinal.setGeometry(QtCore.QRect(1140, 60, 111, 41))
        self.addDataFinal.setObjectName("addDataFinal")
        self.recebeDataFinal = QtWidgets.QLineEdit(self.centralwidget)
        self.recebeDataFinal.setGeometry(QtCore.QRect(660, 60, 461, 41))
        self.recebeDataFinal.setObjectName("recebeDataFinal")
        self.labelGrafico = QtWidgets.QLabel(self.centralwidget)
        self.labelGrafico.setGeometry(QtCore.QRect(20, 170, 1251, 511))
        self.labelGrafico.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.labelGrafico.setObjectName("labelGrafico")
        self.frameGrafico = QtWidgets.QFrame(self.centralwidget)
        self.frameGrafico.setGeometry(QtCore.QRect(20, 170, 1231, 511))
        self.frameGrafico.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameGrafico.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameGrafico.setObjectName("frameGrafico")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameGrafico)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.horizontalLayout.addWidget(self.canvas)
        displayGrafico.setCentralWidget(self.centralwidget)

        self.retranslateUi(displayGrafico)
        QtCore.QMetaObject.connectSlotsByName(displayGrafico)

    def retranslateUi(self, displayGrafico):
        _translate = QtCore.QCoreApplication.translate
        displayGrafico.setWindowTitle(_translate("displayGrafico", "Gráficos de Ações"))
        self.addLista.setText(_translate("displayGrafico", "Adicionar ação"))
        self.limpaLista.setText(_translate("displayGrafico", "Limpar lista"))
        self.geraGrafico.setText(_translate("displayGrafico", "Gerar gráfico"))
        self.Normalizar.setText(_translate("displayGrafico", "Gerar gráfico normalizado"))
        self.recebeAcao.setPlaceholderText(_translate("displayGrafico", "Digite a ação. ex: TECN3.SA"))
        self.recebeDataInicio.setPlaceholderText(_translate("displayGrafico", "Digite a data no formato ano-mês-dia. ex: 2022-20-10"))
        self.addDataInicial.setText(_translate("displayGrafico", "Data inicial"))
        self.addDataFinal.setText(_translate("displayGrafico", "Data final"))
        self.recebeDataFinal.setPlaceholderText(_translate("displayGrafico", "Digite a data no formato ano-mês-dia. ex: 2022-20-10"))
        self.labelGrafico.setText(_translate("displayGrafico", "Grafico:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    displayGrafico = QtWidgets.QMainWindow()
    ui = Ui_displayGrafico()
    ui.setupUi(displayGrafico)
    displayGrafico.show()
    sys.exit(app.exec_())
