from PyQt5 import QtCore, QtGui, QtWidgets
from ui import ui_main, ui_others, ui_simulate, ui_loading, ui_result
from ui.outputs import ui_table, canvas, ui_2d_plot
from process import Simulation

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import pandas as pd
from utility import resource_path

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.width = 800
        self.height = 600

        self.setGeometry(200, 200, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.show()
        self.show_UIMainWindow()
        self.setMenuBar()

        self.flag_simulate = False
    
    def setMenuBar(self):
        self.menubar = self.menuBar()

        # Define action
        self.simulate_action = QtWidgets.QAction('New Simulation')
        self.info_action = QtWidgets.QAction('Info')
        self.help_action = QtWidgets.QAction('Help')
        self.exit_action = QtWidgets.QAction('Exit')
        
        # Add action to menu bar
        self.simulation_menu = self.menubar.addMenu('Simulation')
        self.simulation_menu.addAction(self.simulate_action)
        self.simulation_menu.addAction(self.exit_action)

        self.others = self.menubar.addMenu('Others')
        self.others.addAction(self.info_action)
        self.others.addAction(self.help_action)

        # What to do when actions are clicked
        self.simulate_action.setShortcut('Ctrl+R')
        self.simulate_action.triggered.connect(self.simulateMenuFunction)

        self.info_action.setShortcut('Ctrl+I')
        self.info_action.triggered.connect(self.show_UIInfo)

        self.help_action.setShortcut('Ctrl+E')
        self.help_action.triggered.connect(self.show_UIHelp)

        self.exit_action.setShortcut('Ctrl+W')
        self.exit_action.triggered.connect(self.exitMenuFunction)
        
        # To display menu bar in MacOS
        self.menubar.setNativeMenuBar(False)

    def closeEvent(self, event):
        self.event = event
        self.exitMenuFunction()

    # Function to handle event in menu bar
    def simulateMenuFunction(self):
        if self.flag_simulate:
            self.newSimulationConfirmation()
        else:
            self.show_UISimulate()

    def exitMenuFunction(self):
        self.msg = QtWidgets.QMessageBox(self)
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText(
            "Are you sure do you want to quit?")
        
        self.msg.setWindowTitle("Exit")
        self.msg.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        self.msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
        self.msg.buttonClicked.connect(self.quitApp)
        self.msg.exec_()

    def quitApp(self, i):
        if i.text() == '&Yes':
            QtWidgets.qApp.quit()
        else:
            self.event.ignore()

    # Function making sure user when create new simulation
    def newSimulationConfirmation(self):
        self.msg = QtWidgets.QMessageBox(self)
        self.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.msg.setText(
            "Are you sure to create new simulation?")
        self.msg.setInformativeText(
            "If you click Yes, all of your input will be set to 0")
        self.msg.setWindowTitle("New Simulation")
        self.msg.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        self.msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
        self.msg.buttonClicked.connect(self.createNewSimulation)
        self.msg.exec_()

    def createNewSimulation(self, i):
        if i.text() == '&Yes':
            self.show_UISimulate()

    # Functions to show ui
    def show_UIMainWindow(self):
        self.ui_main = ui_main.UIMainWindow(self)
        self.setWindowTitle("Welcome")
        self.setCentralWidget(self.ui_main)
        self.show()
    
        # self.btnSimulate = self.ui_main.btnSimulateMenu
        # self.btnSimulate.clicked.connect(self.show_UISimulate)
        # self.btnSimulate.adjustSize()

    def show_UIInfo(self):
        self.ui_info = ui_others.UIOthers(self, titleTxt='About This Program', contentTxt=("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                      "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                      "p, li { white-space: pre-wrap; }\n"
                                      "</style></head><body style=\" font-size:13px; font-weight:400; font-style:normal;\">\n"
                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18px;\">Welcome to the air pollution simulation program!</span></p>\n"
                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:18px;\"><br /></p>\n"
                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18px;\">This program is created to simulate air pollution using 1D advection-diffusion equation with Forward Time Backward Space Central Space numerical scheme. Backward difference method is applied to first derivative of space-axis and Central difference method is applied to second derivative of space-axis.</span></p>\n"
                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:18px;\"><br /></p>\n"
                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18px;\">Illustration of simulation:</span></p>\n"
                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:18px;\"><br /></p>\n"
                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18px;\"><img src=\""+resource_path('img/illustration.jpg')+"\" width=500 height=300></span></p>\n"
                                      "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\'; font-size:18px;\"><br /></p>\n"
                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18px;\">The source of the pollutant is located at 0 cm.</span></p>\n"
                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18px;\">The wind inside the space will move from left to right (position 0 to the far most position of space).</span></p></body></html>"
                                      "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:18px;\">The length of the space is represented by L.</span></p></body></html>"))
        self.setWindowTitle('Info')
        self.setCentralWidget(self.ui_info)
        self.show()

    def show_UIHelp(self):
        self.ui_help = ui_others.UIOthers(self, titleTxt='How to Use This Program', contentTxt=("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                                                "p, li { white-space: pre-wrap; }\n"
                                                                                                "</style></head><body style=\" font-size:13px; font-weight:400; font-style:normal;\">\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">1. Create new simulation from menu bar or using the shortcut Ctrl+R(Windows/Linux) Cmd+R(MacOS) or by clicking the button on the first view of this program.</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">2. Input your data. You can use the sample data by checking the Use Sample Data checkbox.</span></p>\n"
                                                                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman\'; font-size:18px;\"><br /></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">Here\'s some explanation about each field:</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">    a. Length (L): represents the 1D length of space in cm, with maximum input 99.99 cm.</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">    b. Observation Duration (T): represents the duration of the simulation in seconds with maximum input 99.999 seconds.</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">    c. Time step: represents the time step that will be used by 1D advection-diffusion model. This time step will be validated using von Neumann analysis to ensure the stability of the model.</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">    d. Initial Concentration: represents the amount of concentration in the space before the simulation started where 0 represents no pollutant at all in the space and 1 represents the space is fully polluted</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">    e. Wind speed (v): represents the speed of the wind inside the space since wind is also responsible to spread the pollutant.</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">    f. Diffusion coefficient (D): represents the pollutant diffusion coefficient. Since each compounds has its own characteristic, so the way they spread and how fast they spread is different from each other.</span></p>\n"
                                                                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px;\"><br /></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">All of your input will be validated. If you give invalid input(s), you can hover the warning icon beside the field to know more information about your input.</span></p>\n"
                                                                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px;\"><br /></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">If you give the valid input, you can press the Simulate button.</span></p>\n"
                                                                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px;\"><br /></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">3. If the loading is finished, on the left side there will information that is used for the simulation. It basically your own input. You can choose what kind of output you want.</span></p>\n"
                                                                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px;\"><br /></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">There are 3 type of outputs:</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">    a. Summary</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">        Summary is the default output of the simulation. You can see what is happening in the simulation step-by-step through the table that is shown. Also, there is some explanations about the output and their meaning.</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">        You can also export the table into .xlsx file or .csv by clicking the Export button on the left side.</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">    b. 2D graph</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">        2D graph mode shows the 2D graph of the simulation. It shows the amount of concentration of pollutant in that space in each second.</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">        You can compare the amount of concentration at given time by using the form below the image. For example, you can compare the amount of concentration at t=0s, t=5s, and t=6s. If you click the Plot button, you can see the graph of that comparison.</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">        Also, if you want to save the 2D graph, you can save it by clicking the &gt;&gt; button above the graph and then click Save (&gt;&gt; then Save).</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">    c. 3D graph</span></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">        3D graph mode shows the 3D graph of that simulation. The x-axis represents position in space,  y-axis represents temporal in time, and z-axis represents the amount of concentration of the pollutant.</span></p>\n"
                                                                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18px;\"><br /></p>\n"
                                                                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">If you want to change some of your input, you can use the Back button on the left side. It will open the input simulation form again with each fields has already been filled with your previous input. You can change it as you need.</span></p></body></html>"))
        self.setWindowTitle('Help')
        self.setCentralWidget(self.ui_help)
        self.show()

    def show_UISimulate(self):
        self.flag_simulate = True

        self.i_icon = QtGui.QPixmap(resource_path('img/i.png'))
        self.i_icon = self.i_icon.scaled(QtCore.QSize(15, 15))

        self.warning_icon = QtGui.QPixmap(resource_path('img/warning.png'))
        self.warning_icon = self.warning_icon.scaled(QtCore.QSize(15, 15))

        self.ui_simulate = ui_simulate.UISimulate(self)
        self.setWindowTitle('Simulation')
        self.setCentralWidget(self.ui_simulate)
        self.show()

        self.sampleData = {
            'L': 25.0,
            'T1': 5.0,
            'C0': 0.0,
            'v': 2.0,
            'D': 1.0,
            'dt': 0.05,
        }

        # Event
        self.ui_simulate.checkSampleData.stateChanged.connect(
            lambda: self.generateSampleData(self.sampleData))
        self.ui_simulate.btnReset.clicked.connect(self.resetConfirmation)
        self.ui_simulate.btnSimulate.clicked.connect(self.validateField)
        
        # Change checkbox to false if there is any changes to input field
        self.ui_simulate.inputL.valueChanged.connect(
            lambda: self.checkValueChanged('L', self.sampleData['L']))
        self.ui_simulate.inputT1.valueChanged.connect(
            lambda: self.checkValueChanged('T1', self.sampleData['T1']))
        self.ui_simulate.inputTimeStep.valueChanged.connect(
            lambda: self.checkValueChanged('dt', self.sampleData['dt']))
        self.ui_simulate.inputInitialConcentration.valueChanged.connect(
            lambda: self.checkValueChanged('C0', self.sampleData['C0']))
        self.ui_simulate.inputV.valueChanged.connect(
            lambda: self.checkValueChanged('v', self.sampleData['v']))
        self.ui_simulate.inputD.valueChanged.connect(
            lambda: self.checkValueChanged('D', self.sampleData['D']))
    
    def show_UILoading(self):
        self.ui_loading = ui_loading.UILoading(self)
        self.setWindowTitle('Loading...')
        self.ui_loading.progressBar.setRange(0,100)
        self.setCentralWidget(self.ui_loading)
        self.show()

        self.processingData(self.ui_loading.progressBar, self.userInput)

    def show_UIResult(self):
        QtGui.QPixmapCache.clear()

        self.userTimeInput = list()

        self.result = self.runnable.simulate.simulationResult
        # self.userInput = self.runnable.userInput

        self.ui_result = ui_result.UIResult(self)
        self.setWindowTitle('Simulation Result')
        self.setCentralWidget(self.ui_result)
        self.show()

        self.ui_result.displaySettings.currentIndexChanged.connect(self.changeOutputWidget)

        self.ui_result.displaySettings.addItem('Table')
        self.ui_result.displaySettings.addItem('2D Graph')
        self.ui_result.displaySettings.addItem('3D Graph')

        # Instantiate output widgets
        self.ui_table = ui_table.UITable(self)
        self.show_UI2DPlot()
        self.plot_2d = canvas.Canvas2D()
        self.plot_3d = canvas.Canvas3D()

        self.toolbar_2d = NavigationToolbar(self.plot_2d, self)

        # Add values to ui_2d_plot
        self.ui_2d_plot.widget2DPlot.addWidget(self.toolbar_2d)
        self.ui_2d_plot.widget2DPlot.addWidget(self.plot_2d)
        self.ui_2d_plot.labelPlotInfo.setPixmap(self.i_icon)
        self.ui_2d_plot.inputPlotTime.setMaximum(int(self.userInput['T']))
        self.ui_2d_plot.setToolTip('Input integer time within range [0-'+str(int(self.userInput['T']))+']')
        
        # Set Values to output widgets
        self.setTableWidgetValue(table=self.ui_table.tableWidgetResult)
        self.plot_2d.drawGraph(self.result['x'], self.result['t'], self.result['C'])
        self.plot_3d.drawGraph(self.result['x'], self.result['t'], self.result['C'])

        # Add output widgets to QStackedWidget
        self.ui_result.outputWidget.addWidget(self.ui_table)
        self.ui_result.outputWidget.addWidget(self.ui_2d_plot)
        self.ui_result.outputWidget.addWidget(self.plot_3d)

        self.ui_2d_plot.btnClearPlot.clicked.connect(self.clearPlot)
        self.ui_2d_plot.btnPlot.clicked.connect(self.processTimePlot)

        self.ui_result.labelDataL.setText(str(self.userInput['L']))
        self.ui_result.labelDataT.setText(str(self.userInput['T']))
        self.ui_result.labelDataInitialConcentration.setText(
            str(self.userInput['initial_condition']))
        self.ui_result.labelDataDt.setText(str(self.userInput['dt']))
        self.ui_result.labelDataV.setText(str(self.userInput['v']))
        self.ui_result.labelDataD.setText(str(self.userInput['D']))

        self.ui_result.btnBack.clicked.connect(
            lambda: self.backToSimulate(self.userInput))
        self.ui_result.btnExport.clicked.connect(self.exportTable)
    
    def show_UI2DPlot(self):
        self.ui_2d_plot = ui_2d_plot.UI2DWidget(self)
        self.show()

    # Function to handle event in ui_result
    def backToSimulate(self, userInput):
        # print(userInput)

        self.show_UISimulate()

        self.ui_simulate.inputL.setValue(userInput['L'])
        self.ui_simulate.inputT1.setValue(userInput['T'])
        self.ui_simulate.inputInitialConcentration.setValue(userInput['initial_condition'])
        self.ui_simulate.inputTimeStep.setValue(userInput['dt'])
        self.ui_simulate.inputV.setValue(userInput['v'])
        self.ui_simulate.inputD.setValue(userInput['D'])

    def changeOutputWidget(self, value):
        if value != 0:
            if value == 1:
                # 2D graph -> idx=1
                QtWidgets.QApplication.processEvents()
                # pass
            elif value == 2:
                # 3D graph -> idx=2
                self.ui_result.outputWidget.update()
                QtWidgets.QApplication.processEvents()
                # pass
            self.ui_result.btnExport.hide()
        else:
            # Table -> idx=0
            self.ui_result.btnExport.show()
        self.ui_result.outputWidget.setCurrentIndex(value)
        QtWidgets.QApplication.processEvents()

    def setTableWidgetValue(self, table):
        # Set Table Header
        # Make sure the table is read-only
        table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        table.setFocusPolicy(QtCore.Qt.NoFocus)
        table.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)

        table.setColumnCount(len(self.result['x']))
        table.setRowCount(len(self.result['t']))

        # Set table header
        self.horizontalHeaderLabel = [str(round(header,4))+' cm' for header in self.result['x']]
        table.setHorizontalHeaderLabels(self.horizontalHeaderLabel)
        self.verticalHeaderLabel = [str(round(header,4)).ljust(4,'0')+' s' for header in self.result['t']]
        table.setVerticalHeaderLabels(self.verticalHeaderLabel)

        # Resize column according to its content
        header = table.horizontalHeader()
        for j in range(table.columnCount()):
            header.setSectionResizeMode(
                j, QtWidgets.QHeaderView.ResizeToContents)

        # Set table contents
        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                table.setItem(i, j, QtWidgets.QTableWidgetItem(str(self.result['C'][i,j])))

    def exportTable(self):
        self.options = QtWidgets.QFileDialog.Options()
        # self.options |= QtWidgets.QFileDialog.DontUseNativeDialog
        self.fileName, self.type = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export Table", "", "Excel Spreadsheet (*.xlsx);;Comma Separated Value (*.csv)", options=self.options)
        if self.fileName:
            self.df = pd.DataFrame(
                data=self.result['C'], columns=self.horizontalHeaderLabel, index=self.verticalHeaderLabel)
            if 'xlsx' in self.type:
                self.df.to_excel(self.fileName)
            elif 'csv' in self.type:
                self.df.to_csv(self.fileName)

    def processTimePlot(self):
        if self.ui_2d_plot.inputPlotTime.value() not in self.userTimeInput:
            self.userTimeInput.append(self.ui_2d_plot.inputPlotTime.value())
            self.userTimeInput.sort()
            self.plot_2d.drawGraph(self.result['x'], self.result['t'], self.result['C'], self.userTimeInput)
        QtWidgets.QApplication.processEvents()

    def clearPlot(self):
        self.userTimeInput = list()
        self.plot_2d.clearGraph()

    # Function to handle event in ui_simulate
    def generateSampleData(self, data):
        # Sample data:
        # L = 25 cm
        # T = 5 s
        # C0 = 0
        # v = 2
        # D = 1
        # dt = 0.05
        if self.ui_simulate.checkSampleData.isChecked():
            if self.ui_simulate.inputL.value() != data['L']:
                self.ui_simulate.inputL.setValue(data['L'])

            if self.ui_simulate.inputT1.value() != data['T1']:
                self.ui_simulate.inputT1.setValue(data['T1'])

            if self.ui_simulate.inputTimeStep.value() != data['dt']:
                self.ui_simulate.inputTimeStep.setValue(data['dt'])

            if self.ui_simulate.inputInitialConcentration.value() != data['C0']:
                self.ui_simulate.inputInitialConcentration.setValue(data['C0'])

            if self.ui_simulate.inputV.value() != data['v']:
                self.ui_simulate.inputV.setValue(data['v'])

            if self.ui_simulate.inputD.value() != data['D']:
                self.ui_simulate.inputD.setValue(data['D'])

    def checkValueChanged(self, field, sampleValue):
        if self.ui_simulate.checkSampleData.isChecked():
            if field == 'L':
                if self.ui_simulate.inputL.value() != sampleValue:
                    self.ui_simulate.checkSampleData.setCheckState(False)
            if field == 'T1':
                if self.ui_simulate.inputT1.value() != sampleValue:
                    self.ui_simulate.checkSampleData.setCheckState(False)
            if field == 'dt':
                if self.ui_simulate.inputTimeStep.value() != sampleValue:
                    self.ui_simulate.checkSampleData.setCheckState(False)
            if field == 'C0':
                if self.ui_simulate.inputInitialConcentration.value() != sampleValue:
                    self.ui_simulate.checkSampleData.setCheckState(False)
            if field == 'v':
                if self.ui_simulate.inputV.value() != sampleValue:
                    self.ui_simulate.checkSampleData.setCheckState(False)
            if field == 'D':
                if self.ui_simulate.inputD.value() != sampleValue:
                    self.ui_simulate.checkSampleData.setCheckState(False)

    def resetConfirmation(self):
        self.ui_simulate.msg = QtWidgets.QMessageBox(self)
        self.ui_simulate.msg.setIcon(QtWidgets.QMessageBox.Warning)
        self.ui_simulate.msg.setText("Are you sure to reset all field to zero?")
        self.ui_simulate.msg.setInformativeText(
            "If you click Yes, all field will be set to 0")
        self.ui_simulate.msg.setWindowTitle("Reset all Field")
        self.ui_simulate.msg.setStandardButtons(
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        self.ui_simulate.msg.setDefaultButton(QtWidgets.QMessageBox.Yes)
        self.ui_simulate.msg.buttonClicked.connect(self.resetAllField)
        self.ui_simulate.msg.exec_()

    def resetAllField(self, i):
        if i.text() == '&Yes':
            QtGui.QPixmapCache.clear()

            self.ui_simulate.inputL.setValue(0)
            self.ui_simulate.inputT1.setValue(0)
            self.ui_simulate.inputTimeStep.setValue(0)
            self.ui_simulate.inputInitialConcentration.setValue(0)
            self.ui_simulate.inputV.setValue(0)
            self.ui_simulate.inputD.setValue(0)

            self.ui_simulate.infoTimeStep.setPixmap(self.i_icon)
            self.ui_simulate.infoTimeStep.setToolTip(
                "Input time step for simulation in second")
            self.ui_simulate.infoTimeStep.setStyleSheet(
                "QToolTip{color:black;}")

            self.ui_simulate.infoD.setPixmap(self.i_icon)
            self.ui_simulate.infoD.setToolTip(
                "Input diffusion coefficient of polutant")
            self.ui_simulate.infoD.setStyleSheet("QToolTip{color:black;}")

    def validateField(self):
        QtGui.QPixmapCache.clear()

        self.flagZeroField = []

        self.msg = QtWidgets.QMessageBox(self)
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setText("Invalid Input!")
        self.msg.setInformativeText("For more information, please hover to red icon next to the field")
        self.msg.setWindowTitle("Invalid Input")
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        # All field can not be zero
        self.L = self.ui_simulate.inputL.value()
        self.T = self.ui_simulate.inputT1.value()
        self.v = self.ui_simulate.inputV.value()
        self.dt = self.ui_simulate.inputTimeStep.value()
        self.D = self.ui_simulate.inputD.value()

        if self.L == 0:
            self.ui_simulate.infoL.setPixmap(self.warning_icon)
            self.ui_simulate.infoL.setToolTip(
                "Length can not be 0")
            self.ui_simulate.infoL.setStyleSheet("QToolTip{color:red;}")
            QtWidgets.QApplication.processEvents()
            self.flagZeroField.append(True)
        elif self.L != 0:
            self.ui_simulate.infoL.setPixmap(self.i_icon)
            self.ui_simulate.infoL.setToolTip(
                "Input length of space in cm")
            self.ui_simulate.infoL.setStyleSheet("QToolTip{color:black;}")
            QtWidgets.QApplication.processEvents()
        
        if self.T == 0:
            self.ui_simulate.infoT1.setPixmap(self.warning_icon)
            self.ui_simulate.infoT1.setToolTip(
                "Duration can not be 0")
            self.ui_simulate.infoT1.setStyleSheet("QToolTip{color:red;}")
            QtWidgets.QApplication.processEvents()
            self.flagZeroField.append(True)
            
        elif self.T != 0:
            self.ui_simulate.infoT1.setPixmap(self.i_icon)
            self.ui_simulate.infoT1.setToolTip(
                "Input simulation duration in second")
            self.ui_simulate.infoT1.setStyleSheet("QToolTip{color:black;}")
            QtWidgets.QApplication.processEvents()

        if self.v == 0:
            self.ui_simulate.infoV.setPixmap(self.warning_icon)
            self.ui_simulate.infoV.setToolTip(
                "Wind speed can not be 0")
            self.ui_simulate.infoV.setStyleSheet("QToolTip{color:red;}")
            QtWidgets.QApplication.processEvents()
            self.flagZeroField.append(True)
        elif self.v != 0:
            self.ui_simulate.infoV.setPixmap(self.i_icon)
            self.ui_simulate.infoV.setToolTip(
                "Input wind speed in space")
            self.ui_simulate.infoV.setStyleSheet("QToolTip{color:black;}")
            QtWidgets.QApplication.processEvents()

        # dt can not be zero
        if self.dt == 0:
            self.ui_simulate.infoTimeStep.setPixmap(self.warning_icon)
            self.ui_simulate.infoTimeStep.setToolTip(
                "Time step can not be 0")
            self.ui_simulate.infoTimeStep.setStyleSheet("QToolTip{color:red;}")
            QtWidgets.QApplication.processEvents()
            self.flagZeroField.append(True)
            
        elif self.dt != 0:
            self.ui_simulate.infoTimeStep.setPixmap(self.i_icon)
            self.ui_simulate.infoTimeStep.setToolTip(
                "Input time step for simulation in second")
            self.ui_simulate.infoTimeStep.setStyleSheet("QToolTip{color:black;}")
            QtWidgets.QApplication.processEvents()

        # D can not be zero
        if self.D == 0:
            self.ui_simulate.infoD.setPixmap(self.warning_icon)
            self.ui_simulate.infoD.setToolTip('D can not be 0')
            self.ui_simulate.infoD.setStyleSheet("QToolTip{color:red;}")

            QtWidgets.QApplication.processEvents()
            self.flagZeroField.append(True)
            
        elif self.D != 0:
            self.ui_simulate.infoD.setPixmap(self.i_icon)
            self.ui_simulate.infoD.setToolTip(
                "Input diffusion coefficient of polutant")
            self.ui_simulate.infoD.setStyleSheet("QToolTip{color:black;}")
            QtWidgets.QApplication.processEvents()
        
        if any(self.flagZeroField):
            self.msg.exec_()
            return

        # Validate time step with neumann condition, dx=0.5
        self.dx = 0.5
        self.dt = self.ui_simulate.inputTimeStep.value()

        if self.dt <= self.dx**2/(2*self.D):
            self.userInput = {
                'L': self.ui_simulate.inputL.value(),
                'T': self.ui_simulate.inputT1.value(),
                'dt': self.ui_simulate.inputTimeStep.value(),
                'dx': 0.5,
                'initial_condition': self.ui_simulate.inputInitialConcentration.value(),
                'v': self.ui_simulate.inputV.value(),
                'D': self.ui_simulate.inputD.value()
            }
            self.show_UILoading()
            
        elif self.dt > self.dx**2/(2*self.D):
            self.ui_simulate.infoTimeStep.setPixmap(self.warning_icon)
            self.ui_simulate.infoTimeStep.setToolTip(
                "Time step must be <= "+str(self.dx**2/(2*self.D)))
            self.ui_simulate.infoTimeStep.setStyleSheet("QToolTip{color:red;}")
            QtWidgets.QApplication.processEvents()
            self.msg.exec_()

    def processingData(self, progressbar, userInput):
        self.runnable = SimulationRunnable(progressbar, userInput)
        self.runnable.signal.done.connect(self.show_UIResult)
        QtCore.QThreadPool.globalInstance().start(self.runnable)


class FinishLoadingSignal(QtCore.QObject):
    done = QtCore.pyqtSignal()


class SimulationRunnable(QtCore.QRunnable):
    def __init__(self, progressbar, userInput: dict):
        QtCore.QRunnable.__init__(self)
        self.progressbar = progressbar
        self.userInput = userInput
        self.simulate = None
        self.signal = FinishLoadingSignal()

    def run(self):
        import time

        self.simulate = Simulation(v=self.userInput['v'], D=self.userInput['D'], a=0, b=self.userInput['L'], t0=0, t1=self.userInput['T'],
                                   initial_condition=self.userInput['initial_condition'], dt=self.userInput['dt'], dx=0.5)
        for i in range(101):
            time.sleep(0.01)
            QtCore.QMetaObject.invokeMethod(
                self.progressbar, "setValue", QtCore.Qt.QueuedConnection, QtCore.Q_ARG(int, i))
        # time.sleep(0.5)
        self.signal.done.emit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(resource_path('img/icon.ico')))
    w = MainWindow()
    sys.exit(app.exec_())
