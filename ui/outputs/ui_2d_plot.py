from PyQt5 import QtCore, QtGui, QtWidgets


class UI2DWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super(UI2DWidget, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 500)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 391, 350))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.widget2DPlot = QtWidgets.QVBoxLayout(
            self.verticalLayoutWidget_2)
        self.widget2DPlot.setContentsMargins(0, 0, 0, 0)
        self.widget2DPlot.setObjectName("widget2DPlot")
        self.btnClearPlot = QtWidgets.QPushButton(self)
        self.btnClearPlot.setGeometry(QtCore.QRect(0, 370, 391, 32))
        self.btnClearPlot.setObjectName("btnClearPlot")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 390, 391, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelPlotInput = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelPlotInput.setObjectName("labelPlotInput")
        self.horizontalLayout.addWidget(self.labelPlotInput)
        self.labelPlotInfo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.labelPlotInfo.setMaximumSize(QtCore.QSize(15, 15))
        self.labelPlotInfo.setObjectName("labelPlotInfo")
        self.horizontalLayout.addWidget(self.labelPlotInfo)
        self.inputPlotTime = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.inputPlotTime.setObjectName("inputPlotTime")
        self.horizontalLayout.addWidget(self.inputPlotTime)
        self.btnPlot = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnPlot.setObjectName("btnPlot")
        self.horizontalLayout.addWidget(self.btnPlot)

        self.retranslateUi()

    def retranslateUi(self):
        self.btnClearPlot.setText("Clear Plot")
        self.labelPlotInput.setText("Draw Plot at time (t)")
        self.btnPlot.setText("Plot")
