from PyQt5 import QtCore, QtGui, QtWidgets
from utility import resource_path
class UISimulate(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UISimulate, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.i_icon = QtGui.QPixmap(resource_path('img/i.png'))
        self.i_icon = self.i_icon.scaled(QtCore.QSize(15, 15))

        self.illustration = QtGui.QPixmap(resource_path('img/illustration.jpg'))
        self.illustration = self.illustration.scaled(QtCore.QSize(500, 250))

        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(200, 0, 500, 500))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.mainLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")

        self.simulationPic = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.simulationPic.setPixmap(self.illustration)
        self.simulationPic.setObjectName("simulationPic")
        self.mainLayout.addWidget(self.simulationPic)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.labelTitle = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        # font.setFamily("Times New Roman")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 1, 1, 1)

        # =================================================================
        self.labelL = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelL.setObjectName("labelL")
        self.gridLayout.addWidget(self.labelL, 1, 0, 1, 1)

        self.infoL = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.infoL.setMaximumSize(QtCore.QSize(15, 15))
        self.infoL.setMinimumSize(QtCore.QSize(15, 15))
        self.infoL.setPixmap(self.i_icon)
        self.infoL.setObjectName("infoL")
        self.gridLayout.addWidget(self.infoL, 1, 1, 1, 1)

        self.inputL = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.inputL.setMaximum(100)
        self.inputL.setObjectName("inputL")
        self.gridLayout.addWidget(self.inputL, 1, 2, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 3, 1, 1)
        # =================================================================
        self.labelT1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelT1.setObjectName("labelT1")
        self.gridLayout.addWidget(self.labelT1, 2, 0, 1, 1)

        self.infoT1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.infoT1.setMaximumSize(QtCore.QSize(15, 15))
        self.infoT1.setPixmap(self.i_icon)
        self.infoT1.setObjectName("infoT1")
        self.gridLayout.addWidget(self.infoT1, 2, 1, 1, 1)

        self.inputT1 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.inputT1.setMaximum(100)
        self.inputT1.setObjectName("inputT1")
        self.gridLayout.addWidget(self.inputT1, 2, 2, 1, 1)

        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 3, 1, 1)
        # =================================================================
        self.labelTimeStep = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelTimeStep.setObjectName("labelTimeStep")
        self.gridLayout.addWidget(self.labelTimeStep, 3, 0, 1, 1)

        self.infoTimeStep = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.infoTimeStep.setMaximumSize(QtCore.QSize(15, 15))
        self.infoTimeStep.setPixmap(self.i_icon)
        self.infoTimeStep.setObjectName("infoTimeStep")
        self.gridLayout.addWidget(self.infoTimeStep, 3, 1, 1, 1)

        self.inputTimeStep = QtWidgets.QDoubleSpinBox(
            self.verticalLayoutWidget)
        self.inputTimeStep.setSingleStep(0.05)
        self.inputTimeStep.setDecimals(3)
        self.inputTimeStep.setObjectName("inputTimeStep")
        self.gridLayout.addWidget(self.inputTimeStep, 3, 2, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 1)
        # =================================================================
        self.labelInitialConcentration = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.labelInitialConcentration.setObjectName(
            "labelInitialConcentration")
        self.gridLayout.addWidget(self.labelInitialConcentration, 4, 0, 1, 1)

        self.infoInitialConcentration = QtWidgets.QLabel(
            self.verticalLayoutWidget)
        self.infoInitialConcentration.setMaximumSize(QtCore.QSize(15, 15))
        self.infoInitialConcentration.setPixmap(self.i_icon)
        self.infoInitialConcentration.setObjectName("infoInitialConcentration")
        self.gridLayout.addWidget(self.infoInitialConcentration, 4, 1, 1, 1)

        self.inputInitialConcentration = QtWidgets.QDoubleSpinBox(
            self.verticalLayoutWidget)
        self.inputInitialConcentration.setMaximum(1.0)
        self.inputInitialConcentration.setSingleStep(0.1)
        self.inputInitialConcentration.setObjectName(
            "inputInitialConcentration")
        self.gridLayout.addWidget(self.inputInitialConcentration, 4, 2, 1, 1)

        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 3, 1, 1)
        # =================================================================
        self.labelV = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelV.setObjectName("labelV")
        self.gridLayout.addWidget(self.labelV, 5, 0, 1, 1)

        self.infoV = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.infoV.setMaximumSize(QtCore.QSize(15, 15))
        self.infoV.setPixmap(self.i_icon)
        self.infoV.setObjectName("infoV")
        self.gridLayout.addWidget(self.infoV, 5, 1, 1, 1)

        self.inputV = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.inputV.setObjectName("inputV")
        self.gridLayout.addWidget(self.inputV, 5, 2, 1, 1)

        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 3, 1, 1)
        # =================================================================
        self.labelD = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labelD.setObjectName("labelD")
        self.gridLayout.addWidget(self.labelD, 6, 0, 1, 1)

        self.infoD = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.infoD.setMaximumSize(QtCore.QSize(15, 15))
        self.infoD.setPixmap(self.i_icon)
        self.infoD.setObjectName("infoD")
        self.gridLayout.addWidget(self.infoD, 6, 1, 1, 1)

        self.inputD = QtWidgets.QDoubleSpinBox(
            self.verticalLayoutWidget)
        self.inputD.setObjectName("inputD")
        self.gridLayout.addWidget(self.inputD, 6, 2, 1, 1)

        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 3, 1, 1)
        # =================================================================
        self.mainLayout.addLayout(self.gridLayout)

        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(430, 525, 350, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.checkSampleData = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkSampleData.setObjectName("checkSampleData")
        self.horizontalLayout.addWidget(self.checkSampleData)

        self.btnReset = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnReset.setObjectName("btnReset")
        self.horizontalLayout.addWidget(self.btnReset)

        self.btnSimulate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnSimulate.setObjectName("btnSimulate")
        self.horizontalLayout.addWidget(self.btnSimulate)

        self.retranslateUi()

    def retranslateUi(self):
        self.labelTitle.setText("Input Data")
        self.labelL.setText("Length (L)")
        self.labelT1.setText("Observation Duration (T)")
        self.labelTimeStep.setText("Time Step ("+u'\u0394'+"t)")
        self.labelInitialConcentration.setText("Initial Concentration")
        self.labelV.setText("Wind Speed (v)")
        self.labelD.setText("Diffusion Coefficient (D)")

        self.label_2.setText("cm")
        self.label_3.setText("s")
        self.label_4.setText("s")
        self.label_8.setText("cm/s")
        self.label_10.setText("cm" + u'\u00b2' + "/s")

        self.checkSampleData.setText("Use sample data")
        self.btnReset.setText("Reset")
        self.btnSimulate.setText("Simulate")

        self.infoL.setToolTip('Input length of space in cm')
        self.infoL.setStyleSheet("QToolTip{color:black;}")

        self.infoT1.setToolTip('Input simulation duration in second')
        self.infoT1.setStyleSheet("QToolTip{color:black;}")

        self.infoTimeStep.setToolTip(
            'Input time step for simulation in second')
        self.infoTimeStep.setStyleSheet("QToolTip{color:black;}")

        self.infoInitialConcentration.setToolTip(
            'Input concentration rate with input range [0,1]')
        self.infoInitialConcentration.setStyleSheet("QToolTip{color:black;}")

        self.infoV.setToolTip('Input wind speed in space')
        self.infoV.setStyleSheet("QToolTip{color:black;}")

        self.infoD.setToolTip('Input diffusion coefficient of polutant')
        self.infoD.setStyleSheet("QToolTip{color:black;}")
