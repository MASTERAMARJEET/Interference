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
        MainWindow.resize(902, 571)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Slit_Option = QtWidgets.QComboBox(self.centralwidget)
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
        self.gridLayout.addWidget(self.Slit_Option, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.I_Spinbox = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans Unicode")
        font.setPointSize(10)
        self.I_Spinbox.setFont(font)
        self.I_Spinbox.setMaximum(1000)
        self.I_Spinbox.setSingleStep(5)
        self.I_Spinbox.setObjectName("I_Spinbox")
        self.gridLayout.addWidget(self.I_Spinbox, 1, 1, 1, 1)
        self.Pic_box = QtWidgets.QLabel(self.centralwidget)
        self.Pic_box.setAutoFillBackground(True)
        self.Pic_box.setText("")
        self.Pic_box.setObjectName("Pic_box")
        self.gridLayout.addWidget(self.Pic_box, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 902, 26))
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
        self.Slit_Option.setWhatsThis(_translate("MainWindow", "Slit Configuration"))
        self.Slit_Option.setItemText(1, _translate("MainWindow", "DOUBLE SLIT"))
        self.Slit_Option.setItemText(2, _translate("MainWindow", "DOUBLE POINT"))
        self.Slit_Option.setItemText(3, _translate("MainWindow", "MULTIPLE SLIT"))
        self.Slit_Option.setItemText(4, _translate("MainWindow", "MULTIPLE POINT"))
        self.Slit_Option.setItemText(5, _translate("MainWindow", "COUSTOMIZED SLIT"))
        self.pushButton.setText(_translate("MainWindow", "Print me"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

