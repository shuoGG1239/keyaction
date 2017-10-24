# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_exampledialog.ui'
#
# Created: Tue Oct 24 17:24:05 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExampleDialog(object):
    def setupUi(self, ExampleDialog):
        ExampleDialog.setObjectName("ExampleDialog")
        ExampleDialog.resize(529, 349)
        self.plainTextEditCode = QtWidgets.QPlainTextEdit(ExampleDialog)
        self.plainTextEditCode.setGeometry(QtCore.QRect(10, 10, 511, 331))
        self.plainTextEditCode.setReadOnly(True)
        self.plainTextEditCode.setObjectName("plainTextEditCode")

        self.retranslateUi(ExampleDialog)
        QtCore.QMetaObject.connectSlotsByName(ExampleDialog)

    def retranslateUi(self, ExampleDialog):
        _translate = QtCore.QCoreApplication.translate
        ExampleDialog.setWindowTitle(_translate("ExampleDialog", "Code Example"))

