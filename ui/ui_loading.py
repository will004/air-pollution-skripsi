from PyQt5 import QtCore, QtGui, QtWidgets

class UILoading(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UILoading, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 140, 331, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.verticalLayout.addWidget(self.label)
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi()

    def retranslateUi(self):
        self.label.setText("Loading...\n"+"Processing the data")
