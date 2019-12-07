# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Amarjeet\Documents\GitHub\Interference\GUI\A1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 600)
        MainWindow.setSizeIncrement(QtCore.QSize(5, 5))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Intro = QtWidgets.QLabel(self.centralwidget)
        self.Intro.setGeometry(QtCore.QRect(20, 10, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Intro.setFont(font)
        self.Intro.setAutoFillBackground(False)
        self.Intro.setFrameShape(QtWidgets.QFrame.Panel)
        self.Intro.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Intro.setLineWidth(3)
        self.Intro.setScaledContents(True)
        self.Intro.setObjectName("Intro")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(20, 50, 951, 491))
        self.main_frame.setMouseTracking(False)
        self.main_frame.setAcceptDrops(True)
        self.main_frame.setAutoFillBackground(False)
        self.main_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setLineWidth(5)
        self.main_frame.setObjectName("main_frame")
        self.Confirm_button = QtWidgets.QPushButton(self.main_frame)
        self.Confirm_button.setGeometry(QtCore.QRect(90, 420, 241, 46))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Confirm_button.setFont(font)
        self.Confirm_button.setFlat(False)
        self.Confirm_button.setObjectName("Confirm_button")
        self.Simulate_button = QtWidgets.QPushButton(self.main_frame)
        self.Simulate_button.setGeometry(QtCore.QRect(600, 420, 241, 46))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Simulate_button.setFont(font)
        self.Simulate_button.setAutoDefault(False)
        self.Simulate_button.setDefault(False)
        self.Simulate_button.setFlat(False)
        self.Simulate_button.setObjectName("Simulate_button")
        self.Screen_Size_label = QtWidgets.QLabel(self.main_frame)
        self.Screen_Size_label.setGeometry(QtCore.QRect(30, 317, 342, 36))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Screen_Size_label.setFont(font)
        self.Screen_Size_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Screen_Size_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Screen_Size_label.setTextFormat(QtCore.Qt.PlainText)
        self.Screen_Size_label.setObjectName("Screen_Size_label")
        self.Screen_Resolution_label = QtWidgets.QLabel(self.main_frame)
        self.Screen_Resolution_label.setGeometry(QtCore.QRect(30, 364, 342, 36))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Screen_Resolution_label.setFont(font)
        self.Screen_Resolution_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Screen_Resolution_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Screen_Resolution_label.setTextFormat(QtCore.Qt.PlainText)
        self.Screen_Resolution_label.setObjectName("Screen_Resolution_label")
        self.Distance_label = QtWidgets.QLabel(self.main_frame)
        self.Distance_label.setGeometry(QtCore.QRect(30, 78, 342, 36))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Distance_label.setFont(font)
        self.Distance_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Distance_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Distance_label.setTextFormat(QtCore.Qt.PlainText)
        self.Distance_label.setObjectName("Distance_label")
        self.Wavelength_label = QtWidgets.QLabel(self.main_frame)
        self.Wavelength_label.setGeometry(QtCore.QRect(30, 126, 342, 36))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Wavelength_label.setFont(font)
        self.Wavelength_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Wavelength_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Wavelength_label.setTextFormat(QtCore.Qt.PlainText)
        self.Wavelength_label.setObjectName("Wavelength_label")
        self.Slit_Size_label = QtWidgets.QLabel(self.main_frame)
        self.Slit_Size_label.setGeometry(QtCore.QRect(30, 173, 342, 36))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Slit_Size_label.setFont(font)
        self.Slit_Size_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Slit_Size_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Slit_Size_label.setTextFormat(QtCore.Qt.PlainText)
        self.Slit_Size_label.setObjectName("Slit_Size_label")
        self.Slit_Option_label = QtWidgets.QLabel(self.main_frame)
        self.Slit_Option_label.setGeometry(QtCore.QRect(30, 30, 342, 36))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Slit_Option_label.setFont(font)
        self.Slit_Option_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Slit_Option_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Slit_Option_label.setTextFormat(QtCore.Qt.PlainText)
        self.Slit_Option_label.setObjectName("Slit_Option_label")
        self.Slit_Separation_label = QtWidgets.QLabel(self.main_frame)
        self.Slit_Separation_label.setGeometry(QtCore.QRect(30, 221, 342, 36))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Slit_Separation_label.setFont(font)
        self.Slit_Separation_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Slit_Separation_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Slit_Separation_label.setTextFormat(QtCore.Qt.PlainText)
        self.Slit_Separation_label.setObjectName("Slit_Separation_label")
        self.Slit_Resoultion_label = QtWidgets.QLabel(self.main_frame)
        self.Slit_Resoultion_label.setGeometry(QtCore.QRect(30, 269, 342, 36))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Slit_Resoultion_label.setFont(font)
        self.Slit_Resoultion_label.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Slit_Resoultion_label.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Slit_Resoultion_label.setTextFormat(QtCore.Qt.PlainText)
        self.Slit_Resoultion_label.setObjectName("Slit_Resoultion_label")
        self.Slit_Size = QtWidgets.QSpinBox(self.main_frame)
        self.Slit_Size.setEnabled(True)
        self.Slit_Size.setGeometry(QtCore.QRect(390, 172, 142, 36))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.Slit_Size.setFont(font)
        self.Slit_Size.setMaximum(1000)
        self.Slit_Size.setSingleStep(5)
        self.Slit_Size.setObjectName("Slit_Size")
        self.Wavelength = QtWidgets.QDoubleSpinBox(self.main_frame)
        self.Wavelength.setGeometry(QtCore.QRect(390, 125, 142, 36))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(10)
        self.Wavelength.setFont(font)
        self.Wavelength.setAcceptDrops(True)
        self.Wavelength.setFrame(True)
        self.Wavelength.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.Wavelength.setDecimals(3)
        self.Wavelength.setMaximum(999.99)
        self.Wavelength.setSingleStep(0.01)
        self.Wavelength.setObjectName("Wavelength")
        self.Slit_Separation = QtWidgets.QSpinBox(self.main_frame)
        self.Slit_Separation.setGeometry(QtCore.QRect(390, 220, 142, 36))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.Slit_Separation.setFont(font)
        self.Slit_Separation.setMaximum(1000)
        self.Slit_Separation.setSingleStep(5)
        self.Slit_Separation.setObjectName("Slit_Separation")
        self.Slit_Resolution = QtWidgets.QSpinBox(self.main_frame)
        self.Slit_Resolution.setGeometry(QtCore.QRect(390, 268, 142, 36))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.Slit_Resolution.setFont(font)
        self.Slit_Resolution.setMaximum(500)
        self.Slit_Resolution.setSingleStep(5)
        self.Slit_Resolution.setObjectName("Slit_Resolution")
        self.Screen_Size = QtWidgets.QSpinBox(self.main_frame)
        self.Screen_Size.setGeometry(QtCore.QRect(390, 317, 142, 36))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.Screen_Size.setFont(font)
        self.Screen_Size.setMaximum(10000)
        self.Screen_Size.setSingleStep(10)
        self.Screen_Size.setObjectName("Screen_Size")
        self.Screen_Resolution = QtWidgets.QDoubleSpinBox(self.main_frame)
        self.Screen_Resolution.setGeometry(QtCore.QRect(390, 363, 142, 36))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.Screen_Resolution.setFont(font)
        self.Screen_Resolution.setObjectName("Screen_Resolution")
        self.Distance = QtWidgets.QDoubleSpinBox(self.main_frame)
        self.Distance.setGeometry(QtCore.QRect(390, 75, 142, 35))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(10)
        self.Distance.setFont(font)
        self.Distance.setAcceptDrops(True)
        self.Distance.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.Distance.setMaximum(999.99)
        self.Distance.setSingleStep(0.5)
        self.Distance.setObjectName("Distance")
        self.Slit_Option = QtWidgets.QComboBox(self.main_frame)
        self.Slit_Option.setGeometry(QtCore.QRect(390, 30, 142, 35))
        self.Slit_Option.setAutoFillBackground(True)
        self.Slit_Option.setEditable(False)
        self.Slit_Option.setObjectName("Slit_Option")
        self.Slit_Option.addItem("")
        self.Slit_Option.setItemText(0, "SINGLE SLIT")
        self.Slit_Option.addItem("")
        self.Slit_Option.addItem("")
        self.Slit_Option.addItem("")
        self.Slit_Option.addItem("")
        self.Slit_Option.addItem("")
        self.Slit_Resolution_unit_2 = QtWidgets.QLabel(self.main_frame)
        self.Slit_Resolution_unit_2.setGeometry(QtCore.QRect(555, 279, 114, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Slit_Resolution_unit_2.setFont(font)
        self.Slit_Resolution_unit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Slit_Resolution_unit_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Slit_Resolution_unit_2.setTextFormat(QtCore.Qt.PlainText)
        self.Slit_Resolution_unit_2.setObjectName("Slit_Resolution_unit_2")
        self.Screen_Size_unit = QtWidgets.QLabel(self.main_frame)
        self.Screen_Size_unit.setGeometry(QtCore.QRect(555, 327, 103, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Screen_Size_unit.setFont(font)
        self.Screen_Size_unit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Screen_Size_unit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Screen_Size_unit.setTextFormat(QtCore.Qt.PlainText)
        self.Screen_Size_unit.setObjectName("Screen_Size_unit")
        self.Screen_Resolution_unit = QtWidgets.QLabel(self.main_frame)
        self.Screen_Resolution_unit.setGeometry(QtCore.QRect(555, 375, 103, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Screen_Resolution_unit.setFont(font)
        self.Screen_Resolution_unit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Screen_Resolution_unit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Screen_Resolution_unit.setTextFormat(QtCore.Qt.PlainText)
        self.Screen_Resolution_unit.setObjectName("Screen_Resolution_unit")
        self.Distance_unit = QtWidgets.QLabel(self.main_frame)
        self.Distance_unit.setGeometry(QtCore.QRect(555, 86, 107, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Distance_unit.setFont(font)
        self.Distance_unit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Distance_unit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Distance_unit.setTextFormat(QtCore.Qt.PlainText)
        self.Distance_unit.setObjectName("Distance_unit")
        self.Waveength_unit = QtWidgets.QLabel(self.main_frame)
        self.Waveength_unit.setGeometry(QtCore.QRect(555, 134, 114, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Waveength_unit.setFont(font)
        self.Waveength_unit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Waveength_unit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Waveength_unit.setTextFormat(QtCore.Qt.PlainText)
        self.Waveength_unit.setObjectName("Waveength_unit")
        self.Slit_Size_unit = QtWidgets.QLabel(self.main_frame)
        self.Slit_Size_unit.setGeometry(QtCore.QRect(555, 182, 114, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Slit_Size_unit.setFont(font)
        self.Slit_Size_unit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Slit_Size_unit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Slit_Size_unit.setTextFormat(QtCore.Qt.PlainText)
        self.Slit_Size_unit.setObjectName("Slit_Size_unit")
        self.Slit_Resolution_unit = QtWidgets.QLabel(self.main_frame)
        self.Slit_Resolution_unit.setGeometry(QtCore.QRect(555, 230, 114, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Slit_Resolution_unit.setFont(font)
        self.Slit_Resolution_unit.setAutoFillBackground(True)
        self.Slit_Resolution_unit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Slit_Resolution_unit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Slit_Resolution_unit.setTextFormat(QtCore.Qt.PlainText)
        self.Slit_Resolution_unit.setObjectName("Slit_Resolution_unit")
        self.Progress_label = QtWidgets.QLabel(self.main_frame)
        self.Progress_label.setGeometry(QtCore.QRect(750, 30, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        self.Progress_label.setFont(font)
        self.Progress_label.setFrameShape(QtWidgets.QFrame.Box)
        self.Progress_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Progress_label.setObjectName("Progress_label")
        self.Progress_Bar = QtWidgets.QProgressBar(self.main_frame)
        self.Progress_Bar.setGeometry(QtCore.QRect(810, 75, 31, 301))
        self.Progress_Bar.setMaximum(104)
        self.Progress_Bar.setProperty("value", 27)
        self.Progress_Bar.setTextVisible(True)
        self.Progress_Bar.setOrientation(QtCore.Qt.Vertical)
        self.Progress_Bar.setTextDirection(QtWidgets.QProgressBar.BottomToTop)
        self.Progress_Bar.setObjectName("Progress_Bar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 998, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Slit_Option.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Intro.setText(_translate("MainWindow", "Hello! This is a program which gives you back a interference pattern on screen according to the slit that you provide."))
        self.Confirm_button.setText(_translate("MainWindow", "Confirm Parameters"))
        self.Simulate_button.setText(_translate("MainWindow", "Simulate"))
        self.Screen_Size_label.setText(_translate("MainWindow", "Screen Size :"))
        self.Screen_Resolution_label.setText(_translate("MainWindow", "Screen Resolution :"))
        self.Distance_label.setText(_translate("MainWindow", "Distance Of the Screen from the slit :"))
        self.Wavelength_label.setText(_translate("MainWindow", "Wavelength of light being used :"))
        self.Slit_Size_label.setText(_translate("MainWindow", "Slit Size :"))
        self.Slit_Option_label.setText(_translate("MainWindow", "Slit Configuration :"))
        self.Slit_Separation_label.setText(_translate("MainWindow", "Separation between Slits:"))
        self.Slit_Resoultion_label.setText(_translate("MainWindow", "Slit Resolution :"))
        self.Wavelength.setWhatsThis(_translate("MainWindow", "Wavelenght of light being used"))
        self.Wavelength.setAccessibleName(_translate("MainWindow", "Wavelength"))
        self.Wavelength.setAccessibleDescription(_translate("MainWindow", "Wavelenght of light being used"))
        self.Distance.setAccessibleName(_translate("MainWindow", "Distance"))
        self.Slit_Option.setWhatsThis(_translate("MainWindow", "Slit Configuration"))
        self.Slit_Option.setItemText(1, _translate("MainWindow", "DOUBLE SLIT"))
        self.Slit_Option.setItemText(2, _translate("MainWindow", "DOUBLE POINT"))
        self.Slit_Option.setItemText(3, _translate("MainWindow", "MULTIPLE SLIT"))
        self.Slit_Option.setItemText(4, _translate("MainWindow", "MULTIPLE POINT"))
        self.Slit_Option.setItemText(5, _translate("MainWindow", "COUSTOMIZED SLIT"))
        self.Slit_Resolution_unit_2.setText(_translate("MainWindow", "micrometers"))
        self.Screen_Size_unit.setText(_translate("MainWindow", "millimeters"))
        self.Screen_Resolution_unit.setText(_translate("MainWindow", "millimeters"))
        self.Distance_unit.setText(_translate("MainWindow", "centimeters"))
        self.Waveength_unit.setText(_translate("MainWindow", "micrometers"))
        self.Slit_Size_unit.setText(_translate("MainWindow", "micrometers"))
        self.Slit_Resolution_unit.setText(_translate("MainWindow", "micrometers"))
        self.Progress_label.setText(_translate("MainWindow", "Progress Bar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
