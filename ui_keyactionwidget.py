# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_keyactionwidget.ui'
#
# Created: Wed Oct 25 23:23:46 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KeyActionWidget(object):
    def setupUi(self, KeyActionWidget):
        KeyActionWidget.setObjectName("KeyActionWidget")
        KeyActionWidget.resize(684, 434)
        self.label = QtWidgets.QLabel(KeyActionWidget)
        self.label.setGeometry(QtCore.QRect(16, 10, 41, 20))
        self.label.setObjectName("label")
        self.lineEditStart = QtWidgets.QLineEdit(KeyActionWidget)
        self.lineEditStart.setGeometry(QtCore.QRect(60, 10, 141, 20))
        self.lineEditStart.setObjectName("lineEditStart")
        self.label_2 = QtWidgets.QLabel(KeyActionWidget)
        self.label_2.setGeometry(QtCore.QRect(233, 10, 41, 20))
        self.label_2.setObjectName("label_2")
        self.lineEditStop = QtWidgets.QLineEdit(KeyActionWidget)
        self.lineEditStop.setGeometry(QtCore.QRect(293, 10, 141, 20))
        self.lineEditStop.setObjectName("lineEditStop")
        self.lineEditInterval = QtWidgets.QLineEdit(KeyActionWidget)
        self.lineEditInterval.setGeometry(QtCore.QRect(293, 40, 141, 20))
        self.lineEditInterval.setObjectName("lineEditInterval")
        self.label_3 = QtWidgets.QLabel(KeyActionWidget)
        self.label_3.setGeometry(QtCore.QRect(16, 40, 41, 20))
        self.label_3.setObjectName("label_3")
        self.lineEditRetime = QtWidgets.QLineEdit(KeyActionWidget)
        self.lineEditRetime.setGeometry(QtCore.QRect(60, 40, 141, 20))
        self.lineEditRetime.setObjectName("lineEditRetime")
        self.label_4 = QtWidgets.QLabel(KeyActionWidget)
        self.label_4.setGeometry(QtCore.QRect(233, 40, 51, 20))
        self.label_4.setObjectName("label_4")
        self.plainTextEditCodeStart = QtWidgets.QPlainTextEdit(KeyActionWidget)
        self.plainTextEditCodeStart.setGeometry(QtCore.QRect(13, 90, 321, 281))
        self.plainTextEditCodeStart.setObjectName("plainTextEditCodeStart")
        self.label_5 = QtWidgets.QLabel(KeyActionWidget)
        self.label_5.setGeometry(QtCore.QRect(16, 70, 111, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(KeyActionWidget)
        self.label_6.setGeometry(QtCore.QRect(353, 70, 111, 20))
        self.label_6.setObjectName("label_6")
        self.plainTextEditCodeStop = QtWidgets.QPlainTextEdit(KeyActionWidget)
        self.plainTextEditCodeStop.setGeometry(QtCore.QRect(350, 90, 321, 281))
        self.plainTextEditCodeStop.setObjectName("plainTextEditCodeStop")
        self.pushButtonExample = QtWidgets.QPushButton(KeyActionWidget)
        self.pushButtonExample.setGeometry(QtCore.QRect(20, 380, 641, 23))
        self.pushButtonExample.setObjectName("pushButtonExample")
        self.pushButtonRun = QtWidgets.QPushButton(KeyActionWidget)
        self.pushButtonRun.setGeometry(QtCore.QRect(450, 10, 101, 23))
        self.pushButtonRun.setObjectName("pushButtonRun")
        self.pushButtonStop = QtWidgets.QPushButton(KeyActionWidget)
        self.pushButtonStop.setGeometry(QtCore.QRect(450, 40, 101, 23))
        self.pushButtonStop.setObjectName("pushButtonStop")
        self.checkBoxCodeStart = QtWidgets.QCheckBox(KeyActionWidget)
        self.checkBoxCodeStart.setGeometry(QtCore.QRect(131, 73, 21, 16))
        self.checkBoxCodeStart.setText("")
        self.checkBoxCodeStart.setObjectName("checkBoxCodeStart")
        self.checkBoxCodeStop = QtWidgets.QCheckBox(KeyActionWidget)
        self.checkBoxCodeStop.setGeometry(QtCore.QRect(460, 73, 21, 16))
        self.checkBoxCodeStop.setText("")
        self.checkBoxCodeStop.setObjectName("checkBoxCodeStop")
        self.labelStatus = QtWidgets.QLabel(KeyActionWidget)
        self.labelStatus.setGeometry(QtCore.QRect(17, 408, 641, 16))
        self.labelStatus.setObjectName("labelStatus")

        self.retranslateUi(KeyActionWidget)
        QtCore.QMetaObject.connectSlotsByName(KeyActionWidget)

    def retranslateUi(self, KeyActionWidget):
        _translate = QtCore.QCoreApplication.translate
        KeyActionWidget.setWindowTitle(_translate("KeyActionWidget", "KeyAction"))
        self.label.setText(_translate("KeyActionWidget", "Start"))
        self.label_2.setText(_translate("KeyActionWidget", "Stop"))
        self.label_3.setText(_translate("KeyActionWidget", "Retime"))
        self.label_4.setText(_translate("KeyActionWidget", "Interval"))
        self.label_5.setText(_translate("KeyActionWidget", "Start Dynamic code"))
        self.label_6.setText(_translate("KeyActionWidget", "Stop Dynamic code"))
        self.pushButtonExample.setText(_translate("KeyActionWidget", "Code Example"))
        self.pushButtonRun.setText(_translate("KeyActionWidget", "Run"))
        self.pushButtonStop.setText(_translate("KeyActionWidget", "Stop"))
        self.labelStatus.setText(_translate("KeyActionWidget", "Status"))

