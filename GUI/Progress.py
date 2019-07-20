# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Amarjeet\Documents\GitHub\Interference\GUI\Progress.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Calculation Completed")
        Form.resize(371, 106)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(15, 15, 346, 76))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Progress_label = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.Progress_label.setAutoFillBackground(True)
        self.Progress_label.setAlignment(QtCore.Qt.AlignCenter)
        self.Progress_label.setReadOnly(True)
        self.Progress_label.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Progress_label.setClearButtonEnabled(False)
        self.Progress_label.setObjectName("Progress_label")
        self.gridLayout.addWidget(self.Progress_label, 0, 0, 1, 1)
        self.Calculation_progress = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.Calculation_progress.setProperty("value", 24)
        self.Calculation_progress.setObjectName("Calculation_progress")
        self.gridLayout.addWidget(self.Calculation_progress, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Calculation Completed", "Calculation Completed"))
        self.Progress_label.setText(_translate("Calculation Completed", "Progress Bar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    for a in range(100):
        ui.Calculation_progress.setProperty("value",a)

    sys.exit(app.exec_())
    