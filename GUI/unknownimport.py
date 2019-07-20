# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Amarjeet\Documents\GitHub\Interference\GUI\unknown.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.I_Spinbox = QtWidgets.QSpinBox(self.centralwidget)
        self.I_Spinbox.setGeometry(QtCore.QRect(435, 105, 181, 43))
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.I_Spinbox.setFont(font)
        self.I_Spinbox.setMaximum(1000)
        self.I_Spinbox.setSingleStep(5)
        self.I_Spinbox.setObjectName("I_Spinbox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(135, 120, 211, 61))
        self.pushButton.setObjectName("pushButton")
        self.Slit_Option = QtWidgets.QComboBox(self.centralwidget)
        self.Slit_Option.setGeometry(QtCore.QRect(210, 30, 181, 35))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.pushButton.setText(_translate("MainWindow", "Print me"))
        self.Slit_Option.setWhatsThis(_translate("MainWindow", "Slit Configuration"))
        self.Slit_Option.setItemText(1, _translate("MainWindow", "DOUBLE SLIT"))
        self.Slit_Option.setItemText(2, _translate("MainWindow", "DOUBLE POINT"))
        self.Slit_Option.setItemText(3, _translate("MainWindow", "MULTIPLE SLIT"))
        self.Slit_Option.setItemText(4, _translate("MainWindow", "MULTIPLE POINT"))
        self.Slit_Option.setItemText(5, _translate("MainWindow", "COUSTOMIZED SLIT"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

