from PyQt5 import QtCore, QtGui, QtWidgets

class UIMainWindow(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(UIMainWindow, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.width = 800
        self.height = 600

        self.labelJudul = QtWidgets.QLabel(self)
        self.labelJudul.setGeometry(QtCore.QRect(
            self.width//2-391//2, 20, 391, 221))
        font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        font.setPixelSize(24)
        font.setBold(True)
        self.labelJudul.setFont(font)
        self.labelJudul.setAlignment(QtCore.Qt.AlignCenter)
        self.labelJudul.setWordWrap(True)
        self.labelJudul.setObjectName("labelJudul")

        self.labelAuthor = QtWidgets.QLabel(self)
        self.labelAuthor.setGeometry(QtCore.QRect(
            self.width//2-121//2, 250, 121, 61))
        font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        font.setPixelSize(18)
        self.labelAuthor.setFont(font)
        self.labelAuthor.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAuthor.setObjectName("labelAuthor")

        self.labelBinus = QtWidgets.QLabel(self)
        self.labelBinus.setGeometry(QtCore.QRect(
            self.width//2-191//2, 350, 191, 141))
        font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        font.setPixelSize(18)
        font.setBold(True)
        self.labelBinus.setFont(font)
        self.labelBinus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelBinus.setWordWrap(True)
        self.labelBinus.setObjectName("labelBinus")

        # self.btnSimulateMenu = QtWidgets.QPushButton(self)
        # self.btnSimulateMenu.setGeometry(
        #     QtCore.QRect(self.width//2-150//2, 450, 150, 32))
        # self.btnSimulateMenu.setObjectName("btnSimulateMenu")

        self.retranslateUi()

    def retranslateUi(self):
        self.labelJudul.setText(
            "SIMULASI POLUSI UDARA DENGAN MODEL ADVEKSI-DIFUSI DAN METODE BEDA HINGGA")
        self.labelAuthor.setText("Dibuat Oleh\n"
                                 "William\n"
                                 "1901460373")
        self.labelBinus.setText("Binus University\n"
                                "2020")
        # self.btnSimulateMenu.setText("NEW SIMULATION")
