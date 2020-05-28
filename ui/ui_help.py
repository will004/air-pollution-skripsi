from PyQt5 import QtCore, QtGui, QtWidgets

class UIHelp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(UIHelp, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.resize(800, 600)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 761, 561))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.retranslateUi()

    def retranslateUi(self):
        self.label.setText("How to Use This Program")
        self.textBrowser.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                 "p, li { white-space: pre-wrap; }\n"
                                 "</style></head><body style=\" font-family:\'Times New Roman\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">1. Create new simulation from menu bar or using the shortcut Ctrl+R(Windows/Linux) Cmd+R(MacOS) or by clicking the button on the first view of this program.</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">2. Input your data. You can use the sample data by checking the Use Sample Data checkbox.</span></p>\n"
                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:18pt;\"><br /></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">Here\'s some explanation about each field:</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">    a. Length (L): represents the 1D length of space in cm, with maximum input 99.99 cm.</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">    b. Observation Duration (T): represents the duration of the simulation in seconds with maximum input 99.999 seconds.</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">    c. Time step: represents the time step that will be used by 1D advection-diffusion model. This time step will be validated using von Neumann analysis to ensure the stability of the model.</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">    d. Initial Concentration: represents the amount of concentration in the space before the simulation started where 0 represents no pollutant at all in the space and 1 represents the space is fully polluted</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">    e. Wind speed (v): represents the speed of the wind inside the space since wind is also responsible to spread the pollutant.</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">    f. Diffusion coefficient (D): represents the pollutant diffusion coefficient. Since each compounds has its own characteristic, so the way they spread and how fast they spread is different from each other.</span></p>\n"
                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:18pt;\"><br /></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">All of your input will be validated. If you give invalid input(s), you can hover the warning icon beside the field to know more information about your input.</span></p>\n"
                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:18pt;\"><br /></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">If you give the valid input, you can press the Simulate button.</span></p>\n"
                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:18pt;\"><br /></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">3. If the loading is finished, on the left side there will information that is used for the simulation. It basically your own input. You can choose what kind of output you want.</span></p>\n"
                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:18pt;\"><br /></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">There are 3 type of outputs:</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">    a. Summary</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">        Summary is the default output of the simulation. You can see what is happening in the simulation step-by-step through the table that is shown. Also, there is some explanations about the output and their meaning.</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">        You can also export the table into .xlsx file or .csv by clicking the Export button on the left side.</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">    b. 2D graph</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">        2D graph mode shows the 2D graph of the simulation. It shows the amount of concentration of pollutant in that space in each second.</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">        You can compare the amount of concentration at given time by using the form below the image. For example, you can compare the amount of concentration at t=0s, t=5s, and t=6s. If you click the Plot button, you can see the graph of that comparison.</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">        Also, if you want to save the 2D graph, you can save it by clicking the &gt;&gt; button above the graph and then click Save (&gt;&gt; then Save).</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">    c. 3D graph</span></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">        3D graph mode shows the 3D graph of that simulation. The x-axis represents position in space,  y-axis represents temporal in time, and z-axis represents the amount of concentration of the pollutant.</span></p>\n"
                                 "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:18pt;\"><br /></p>\n"
                                 "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\'; font-size:18pt;\">If you want to change some of your input, you can use the Back button on the left side. It will open the input simulation form again with each fields has already been filled with your previous input. You can change it as you need.</span></p></body></html>")
