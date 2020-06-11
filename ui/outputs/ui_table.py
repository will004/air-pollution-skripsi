from PyQt5 import QtCore, QtGui, QtWidgets


class UITable(QtWidgets.QWidget):
    def __init__(self, parent):
        super(UITable, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(400, 500)
        self.labelTitleOutput = QtWidgets.QLabel(self)
        self.labelTitleOutput.setGeometry(QtCore.QRect(0, 0, 91, 41))
        font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitleOutput.setFont(font)
        self.labelTitleOutput.setObjectName("labelTitleOutput")
        self.tableWidgetResult = QtWidgets.QTableWidget(self)
        self.tableWidgetResult.setGeometry(QtCore.QRect(0, 42, 390, 221))
        font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        self.tableWidgetResult.setFont(font)
        self.tableWidgetResult.setObjectName("tableWidgetResult")
        self.tableWidgetResult.setColumnCount(0)
        self.tableWidgetResult.setRowCount(0)
        self.textTable = QtWidgets.QTextBrowser(self)
        self.textTable.setGeometry(QtCore.QRect(0, 280, 390, 211))
        font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        self.textTable.setFont(font)
        self.textTable.setObjectName("textTable")
        self.retranslateUi()


    def retranslateUi(self):
        # self.TableText.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut rhoncus lacus ipsum, vel dictum orci tincidunt eget. Mauris malesuada, purus et mattis fringilla, diam lorem cursus nibh, sit amet volutpat libero sem eu justo. Vestibulum convallis massa eget congue ultricies. Nullam vulputate urna a fringilla ornare. Praesent iaculis elit vitae mollis mattis. Nunc vel purus accumsan, ultricies nunc sed, mollis lacus. Sed interdum dui vitae vulputate porttitor. Proin venenatis a orci eget tristique. Sed porta, nibh quis laoreet volutpat, nunc lacus viverra libero, quis venenatis urna eros in nibh. Duis mauris sapien, viverra et lobortis vitae, porttitor sed ligula. Morbi ac molestie nisi. Aliquam erat volutpat. Phasellus bibendum tortor sed odio viverra viverra. Curabitur accumsan molestie arcu eu porttitor. Vivamus dapibus efficitur nisi et convallis. Proin diam ex, tempor ut turpis id, euismod dapibus eros.")
        self.labelTitleOutput.setText("Output")
        self.textTable.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\';\">Each cells represents the concentration of pollutant at one point of time and space.<br>Each columns represents position in the space.<br>Each rows represents one time step in the simulation.<br><br>The source of the pollutant is located at position 0. So, at the beginning of the simulation, the pollutant's concentration is 1 at position 0.</span></p></body></html>")
