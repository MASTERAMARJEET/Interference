import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from math import cos, pi, sqrt
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
# import time


# GUI settings Start:


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Simulator")
        MainWindow.resize(998, 600)
        MainWindow.setSizeIncrement(QtCore.QSize(5, 5))
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Pic_box0 = QtWidgets.QLabel(self.centralwidget)
        self.Pic_box0.setGeometry(QtCore.QRect(0, 0, 1010, 600))
        self.Pic_box0.setText("")
        self.Pic_box0.setObjectName("Pic_box")
        pic0 = QtGui.QPixmap(
            "C:\\Users\\Amarjeet\\Documents\\GitHub\\Interference\\GUI\\B0.png")
        pic0 = pic0.scaled(self.Pic_box0.width(), self.Pic_box0.height())
        self.Pic_box0.setPixmap(pic0)
        self.Pic_box0.setAlignment(QtCore.Qt.AlignCenter)
        self.Intro = QtWidgets.QLabel(self.centralwidget)
        self.Intro.setGeometry(QtCore.QRect(20, 10, 951, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Intro.setFont(font)
        self.Intro.setAutoFillBackground(True)
        self.Intro.setFrameShape(QtWidgets.QFrame.Panel)
        self.Intro.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Intro.setLineWidth(3)
        self.Intro.setObjectName("Intro")
        self.Pic_box = QtWidgets.QLabel(self.centralwidget)
        self.Pic_box.setGeometry(QtCore.QRect(20, 50, 951, 491))
        self.Pic_box.setText("")
        self.Pic_box.setObjectName("Pic_box")
        pic = QtGui.QPixmap(
            "C:\\Users\\Amarjeet\\Documents\\GitHub\\Interference\\GUI\\background4.png")
        pic = pic.scaled(self.Pic_box.width(), self.Pic_box.height())
        self.Pic_box.setPixmap(pic)
        self.Pic_box.setAlignment(QtCore.Qt.AlignCenter)
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
        self.Screen_Size_label.setTextFormat(QtCore.Qt.PlainText)
        self.Screen_Size_label.setObjectName("Screen_Size_label")
        self.Screen_Resolution_label = QtWidgets.QLabel(self.main_frame)
        self.Screen_Resolution_label.setGeometry(
            QtCore.QRect(30, 364, 342, 36))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Screen_Resolution_label.setFont(font)
        self.Screen_Resolution_label.setFrameShape(QtWidgets.QFrame.WinPanel)
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
        self.Slit_Separation_label.setTextFormat(QtCore.Qt.PlainText)
        self.Slit_Separation_label.setObjectName("Slit_Separation_label")
        self.Slit_Plane_Resolution_label = QtWidgets.QLabel(self.main_frame)
        self.Slit_Plane_Resolution_label.setGeometry(
            QtCore.QRect(30, 269, 342, 36))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Slit_Plane_Resolution_label.setFont(font)
        self.Slit_Plane_Resolution_label.setFrameShape(
            QtWidgets.QFrame.WinPanel)
        self.Slit_Plane_Resolution_label.setTextFormat(QtCore.Qt.PlainText)
        self.Slit_Plane_Resolution_label.setObjectName(
            "Slit_Plane_Resolution_label")
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
        self.Slit_Size.setEnabled(True)
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
        self.Slit_Separation.setEnabled(False)
        self.Slit_Plane_Resolution = QtWidgets.QSpinBox(self.main_frame)
        self.Slit_Plane_Resolution.setGeometry(QtCore.QRect(390, 268, 142, 36))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.Slit_Plane_Resolution.setFont(font)
        self.Slit_Plane_Resolution.setMaximum(500)
        self.Slit_Plane_Resolution.setSingleStep(5)
        self.Slit_Plane_Resolution.setObjectName("Slit_Plane_Resolution")
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
        self.Slit_Plane_Resolution_unit_2 = QtWidgets.QLabel(self.main_frame)
        self.Slit_Plane_Resolution_unit_2.setGeometry(
            QtCore.QRect(555, 279, 114, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Slit_Plane_Resolution_unit_2.setFont(font)
        self.Slit_Plane_Resolution_unit_2.setFrameShape(
            QtWidgets.QFrame.NoFrame)
        self.Slit_Plane_Resolution_unit_2.setFrameShadow(
            QtWidgets.QFrame.Plain)
        self.Slit_Plane_Resolution_unit_2.setTextFormat(QtCore.Qt.PlainText)
        self.Slit_Plane_Resolution_unit_2.setObjectName(
            "Slit_Plane_Resolution_unit_2")
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
        self.Screen_Resolution_unit.setGeometry(
            QtCore.QRect(555, 375, 103, 20))
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
        self.Slit_Plane_Resolution_unit = QtWidgets.QLabel(self.main_frame)
        self.Slit_Plane_Resolution_unit.setGeometry(
            QtCore.QRect(555, 230, 114, 20))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Slit_Plane_Resolution_unit.setFont(font)
        self.Slit_Plane_Resolution_unit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Slit_Plane_Resolution_unit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Slit_Plane_Resolution_unit.setTextFormat(QtCore.Qt.PlainText)
        self.Slit_Plane_Resolution_unit.setObjectName(
            "Slit_Plane_Resolution_unit")
        self.Progress_label = QtWidgets.QLabel(self.main_frame)
        self.Progress_label.setGeometry(QtCore.QRect(725, 30, 201, 30))
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
        self.Progress_Bar.setProperty("value", 0)
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

        self.Slit_Option.currentIndexChanged.connect(self.disable)
        self.Confirm_button.clicked.connect(self.param)
        self.Simulate_button.clicked.connect(self.main)

    def disable(self):
        x = self.Slit_Option.currentIndex()

        if x != 0:
            self.Slit_Separation.setEnabled(True)
        else:
            self.Slit_Separation.setEnabled(False)

        if x == 0 or x == 5:
            self.Slit_Size.setEnabled(True)
        else:
            self.Slit_Size.setEnabled(False)

    def param(self):
        configure = self.Slit_Option.currentText()
        D = float(self.Distance.text())
        wvlen = float(self.Wavelength.text())
        slt_sz = float(self.Slit_Size.text())
        slt_sep = float(self.Slit_Separation.text())
        slt_res = float(self.Slit_Plane_Resolution.text())
        scr_sz = float(self.Screen_Size.text())
        scr_res = float(self.Screen_Resolution.text())

        return configure, D, wvlen, slt_sz, slt_sep, slt_res, scr_sz, scr_res

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Simulator", "Simulator"))
        self.Intro.setText(_translate(
            "Simulator", "Hello! This is a program which gives you back a interference pattern on screen according to the slit that you provide."))
        self.Confirm_button.setText(_translate(
            "Simulator", "Confirm Parameters"))
        self.Simulate_button.setText(_translate("Simulator", "Simulate"))
        self.Screen_Size_label.setText(
            _translate("Simulator", "Screen Size :"))
        self.Screen_Resolution_label.setText(
            _translate("Simulator", "Screen Resolution :"))
        self.Distance_label.setText(_translate(
            "Simulator", "Distance Of the Screen from the slit :"))
        self.Wavelength_label.setText(_translate(
            "Simulator", "Wavelength of light being used :"))
        self.Slit_Size_label.setText(_translate("Simulator", "Slit Size :"))
        self.Slit_Option_label.setText(
            _translate("Simulator", "Slit Configuration :"))
        self.Slit_Separation_label.setText(_translate(
            "Simulator", "Separation between Slits:"))
        self.Slit_Plane_Resolution_label.setText(
            _translate("Simulator", "Slit Resolution :"))
        self.Wavelength.setWhatsThis(_translate(
            "Simulator", "Wavelenght of light being used"))
        self.Wavelength.setAccessibleName(
            _translate("Simulator", "Wavelength"))
        self.Wavelength.setAccessibleDescription(
            _translate("Simulator", "Wavelenght of light being used"))
        self.Distance.setAccessibleName(_translate("Simulator", "Distance"))
        self.Slit_Option.setWhatsThis(
            _translate("Simulator", "Slit Configuration"))
        self.Slit_Option.setItemText(1, _translate("Simulator", "DOUBLE SLIT"))
        self.Slit_Option.setItemText(
            2, _translate("Simulator", "DOUBLE POINT"))
        self.Slit_Option.setItemText(3, _translate("Simulator", "TRIPLE SLIT"))
        self.Slit_Option.setItemText(
            4, _translate("Simulator", "TRIPLE POINT"))
        self.Slit_Option.setItemText(
            5, _translate("Simulator", "COUSTOMIZED SLIT"))
        self.Slit_Plane_Resolution_unit_2.setText(
            _translate("Simulator", "micrometers"))
        self.Screen_Size_unit.setText(_translate("Simulator", "millimeters"))
        self.Screen_Resolution_unit.setText(
            _translate("Simulator", "millimeters"))
        self.Distance_unit.setText(_translate("Simulator", "centimeters"))
        self.Waveength_unit.setText(_translate("Simulator", "micrometers"))
        self.Slit_Size_unit.setText(_translate("Simulator", "micrometers"))
        self.Slit_Plane_Resolution_unit.setText(
            _translate("Simulator", "micrometers"))
        self.Progress_label.setText(_translate(
            "MainWindow", "Calculation Progress"))

# GUI settings End:
    @staticmethod
    def main():

        Intro = 'Hello! This is a program which gives you back a interference pattern on screen according to the slit that you provide.'

        I0 = 1.0

        Buffer = ui.param()

        print(Buffer)

        Slit_option, Distance, Wavelength, Slit_Size, Slit_Separation, Slit_Plane_Resolution, Screen_Size, Screen_Resoution = Buffer

        if Slit_option == 'SINGLE SLIT':
            pass

        elif Slit_option == 'DOUBLE SLIT':
            class case1(configurator):

                def create_slit(self, slt_sz, slt_sep, slt_res, scr_sz, scr_res):
                    configurator.create_slit(
                        self, slt_sz, slt_sep, slt_res, scr_sz, scr_res)

                    self.Slit_Grid = int(slt_sep/slt_res)

                    Slit = []
                    for i in range(10):
                        Slit.append([0.0]*(self.Slit_Grid + 1))
                        Slit[i][0] = I0
                        Slit[i][-1] = I0
                    self.slit = Slit
                    return self.slit

            S1 = case1(Slit_option)

        elif Slit_option == 'DOUBLE POINT':
            class case2(configurator):

                def create_slit(self, slt_sz, slt_sep, slt_res, scr_sz, scr_res):
                    configurator.create_slit(
                        self, slt_sz, slt_sep, slt_res, scr_sz, scr_res)

                    self.Slit_Grid = int(slt_sep/slt_res)

                    Slit = []
                    for i in range(1):
                        Slit.append([0.0]*(self.Slit_Grid + 1))
                        Slit[i][0] = I0
                        Slit[i][-1] = I0
                    self.slit = Slit
                    return self.slit

            S1 = case2(Slit_option)

        elif Slit_option == 'TRIPLE SLIT':
            pass

        elif Slit_option == 'TRIPLE POINT':
            class case4(configurator):

                def create_slit(self, slt_sz, slt_sep, slt_res, scr_sz, scr_res):
                    configurator.create_slit(
                        self, slt_sz, slt_sep, slt_res, scr_sz, scr_res)

                    self.Slit_Grid = int(slt_sep/slt_res)

                    Slit = []
                    for i in range(1):
                        Slit.append([0.0]*(2*self.Slit_Grid + 1))
                        Slit[i][0] = I0
                        Slit[i][self.Slit_Grid - 2] = I0
                        Slit[i][-1] = I0
                    self.slit = Slit
                    return self.slit

            S1 = case4(Slit_option)

        Slit = S1.create_slit(Slit_Size, Slit_Separation,
                              Slit_Plane_Resolution, Screen_Size, Screen_Resoution)

        slt_grid, scr_grid, f, g = S1.Slit_Grid, S1.Screen_Grid, S1.A1, S1.A2

        print(Slit)
        beta = (Wavelength*Distance*10)/Slit_Separation
        print(beta)

        W = em_wave('Source', Wavelength*0.001)

        Screen = []

        def Theta(i, j, x, y):
            variable = pi*Slit_Plane_Resolution*abs(sqrt((Distance*g)**2 + (x_point*f-i)**2 + (
                y_point*f-j)**2) - sqrt((Distance*g)**2 + (x_point*f-x)**2 + (y_point*f-y)**2))/Wavelength
            return variable

        def func(x_point, y_point):
            I = 0.0
            for i in range(len(Slit)):
                for j in range(len(Slit[i])):
                    for x in range(i, len(Slit)):
                        for y in range(j, len(Slit[x])):
                            if (x, y) != (i, j):
                                if Slit[x][y] != 0.0 and Slit[i][j] != 0.0:
                                    I = + \
                                        Slit[x][y] + Slit[i][j] + 2 * \
                                        sqrt(Slit[x][y]*Slit[i][j]) * \
                                        (cos(2*Theta(i, j, x, y)))
                                    # print(x,y,i,j)
            return(I)

        p = range(-scr_grid, scr_grid+1)
        q = range(-scr_grid, scr_grid+1)

        for x_point in p:
            M = []
            for y_point in q:
                M.append(func(x_point, y_point))
            Screen.append(M)
            ui.Progress_Bar.setProperty("value", len(Screen)/len(p)*100)

        xtics = [i*(Screen_Resoution) for i in p]
        ytics = [j*(Screen_Resoution) for j in q]

        X, Y = np.meshgrid(xtics, ytics)

        plt.xlabel('X axis (in mm)', fontsize='large')
        plt.ylabel('Y axis (in mm)', fontsize='large')

        plt.contourf(X, Y, Screen, 30, cmap='gray')
        plt.colorbar()
        plt.show()


class configurator:
    def __init__(self, configure):
        self.configuration = configure

    def create_slit(self, slt_sz, slt_sep, slt_res, scr_sz, scr_res):
        self.Slit_Size = slt_sz
        self.Slit_Separation = slt_sep
        self.Slit_Plane_Resolution = slt_res
        self.Screen_Size = scr_sz
        self.Screen_Resoution = scr_res
        self.Slit_Grid = int(slt_sz/slt_res)
        self.Screen_Grid = int((scr_sz)/scr_res)
        self.A1 = scr_res*1000/slt_res
        self.A2 = 10000/slt_res

        Slit = 0.0
        for i in range(2):
            Slit = [Slit]*(self.Slit_Grid)
        self.slit = Slit

        return self.slit


class em_wave():

    c = 3*(10**11)  # unit-> mm/sec
    E = np.array([1, 1, 1])
    phi = 0
    k_unit = np.array([0, 0, 1])  # unit-> 1/mm
    r = np.array([0, 0, 1])  # unit-> 1/mm
    # t = time.time()                           #unit-> sec
    t = 0

    def __init__(self, name, wavelength):
        self.wave_name = name
        self.wavelength = wavelength  # unit-> mm
        self.frequency = self.c/self.wavelength
        self.k = (2*pi/self.wavelength)*self.k_unit
        self.omega = 2*pi*self.frequency

    def __repr__(self):
        return 'This is a wave object which can given all the proprties that a wave should have.For more info. type object.help()'

    def set_eq(self, E, phi):
        self.E = np.array(E)
        self.phi = phi
        self.wave_eq = np.array(
            [P*cos(np.dot(self.k, self.r) - self.omega*self.t + self.phi) for P in self.E])

    def Wave_eq(self, r):
        self.r = np.array(r)/sqrt(sum([p**2 for p in self.r]))
        self.wave_eq = (np.array([P*cos(np.dot(self.k, self.r) - self.omega*self.t + self.phi)
                                  for P in self.E])/sqrt(sum([p**2 for p in self.r])))
        # print(cos(np.dot(self.k,self.r)))
        return self.wave_eq

    def help(self):
        print('This obect has following properties as of now:')
        print(f'wave_name:{self.wave_name}')
        print(f'wavelength:{self.wavelength}')
        print(f'frequency:{self.frequency}')
        print(f'E:{self.E}')
        print(f'k:{self.k}')
        print(f'r:{self.r}')
        print(f'phi:{self.phi}')
        print(f'wave_eq:{self.wave_eq}')


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
