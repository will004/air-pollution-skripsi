from PyQt5 import QtCore, QtGui, QtWidgets

class UIOthers(QtWidgets.QWidget):
    def __init__(self, parent=None, titleTxt='', contentTxt=''):
        super(UIOthers, self).__init__()
        self.setupUi(titleTxt, contentTxt)

    def setupUi(self, titleTxt, contentTxt):
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 5, 780, 560))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        font.setPixelSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi(titleTxt, contentTxt)

    def retranslateUi(self, titleTxt, contentTxt):
        self.label.setText(titleTxt)
        self.textBrowser.setHtml(contentTxt)
        # self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
        #                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        #                          "p, li { white-space: pre-wrap; }\n"
        #                          "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
        #                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18pt;\">Welcome to the air pollution simulation program!</span></p>\n"
        #                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:18pt;\"><br /></p>\n"
        #                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18pt;\">This program is created to simulate air pollution using 1D advection-diffusion equation with Forward Time Backward Space Central Space numerical scheme. Backward difference method is applied to first derivative of space-axis and Central difference method is applied to second derivative of space-axis.</span></p>\n"
        #                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:18pt;\"><br /></p>\n"
        #                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18pt;\">Illustration of simulation:</span></p>\n"
        #                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:18pt;\"><br /></p>\n"
        #                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18pt;\"><img src=\"img/illustration.jpg\" width=500 height=300></span></p>\n"
        #                          "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:18pt;\"><br /></p>\n"
        #                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18pt;\">The source of the pollutant is located at 0 cm.</span></p>\n"
        #                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18pt;\">The wind inside the space will move from left to right (position 0 to the far most position of space).</span></p></body></html>"
        #                          "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18pt;\">The length of the space is represented by L.</span></p></body></html>")
