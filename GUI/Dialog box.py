# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Amarjeet\Documents\GitHub\Interference\GUI\Dialog box.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(367, 200)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(75, 150, 196, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.Question = QtWidgets.QLabel(Dialog)
        self.Question.setGeometry(QtCore.QRect(45, 30, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Question.setFont(font)
        self.Question.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Question.setAutoFillBackground(True)
        self.Question.setScaledContents(False)
        self.Question.setAlignment(QtCore.Qt.AlignCenter)
        self.Question.setObjectName("Question")
        self.spinBox = QtWidgets.QSpinBox(Dialog)
        self.spinBox.setGeometry(QtCore.QRect(120, 90, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setReadOnly(False)
        self.spinBox.setMinimum(3)
        self.spinBox.setMaximum(5)
        self.spinBox.setProperty("value", 3)
        self.spinBox.setObjectName("spinBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Question.setText(_translate("Dialog", "Choose the number of slits required:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

