# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_keyactionwidget.ui'
#
# Created: Fri Oct 27 17:01:18 2017
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KeyActionWidget(object):
    def setupUi(self, KeyActionWidget):
        KeyActionWidget.setObjectName("KeyActionWidget")
        KeyActionWidget.resize(478, 509)
        self.label = QtWidgets.QLabel(KeyActionWidget)
        self.label.setGeometry(QtCore.QRect(30, 13, 41, 20))
        self.label.setObjectName("label")
        self.lineEditStart = QtWidgets.QLineEdit(KeyActionWidget)
        self.lineEditStart.setGeometry(QtCore.QRect(74, 13, 141, 25))
        self.lineEditStart.setObjectName("lineEditStart")
        self.label_2 = QtWidgets.QLabel(KeyActionWidget)
        self.label_2.setGeometry(QtCore.QRect(30, 51, 41, 20))
        self.label_2.setObjectName("label_2")
        self.lineEditStop = QtWidgets.QLineEdit(KeyActionWidget)
        self.lineEditStop.setGeometry(QtCore.QRect(74, 51, 141, 25))
        self.lineEditStop.setObjectName("lineEditStop")
        self.pushButtonRun = QtWidgets.QPushButton(KeyActionWidget)
        self.pushButtonRun.setGeometry(QtCore.QRect(234, 13, 121, 23))
        self.pushButtonRun.setObjectName("pushButtonRun")
        self.labelStatus = QtWidgets.QLabel(KeyActionWidget)
        self.labelStatus.setGeometry(QtCore.QRect(16, 473, 641, 16))
        self.labelStatus.setObjectName("labelStatus")
        self.groupBoxRadio = QtWidgets.QGroupBox(KeyActionWidget)
        self.groupBoxRadio.setGeometry(QtCore.QRect(234, 51, 121, 27))
        self.groupBoxRadio.setTitle("")
        self.groupBoxRadio.setObjectName("groupBoxRadio")
        self.radioButtonExit = QtWidgets.QRadioButton(self.groupBoxRadio)
        self.radioButtonExit.setGeometry(QtCore.QRect(10, 5, 61, 16))
        self.radioButtonExit.setChecked(True)
        self.radioButtonExit.setObjectName("radioButtonExit")
        self.radioButtonStop = QtWidgets.QRadioButton(self.groupBoxRadio)
        self.radioButtonStop.setGeometry(QtCore.QRect(60, 5, 51, 16))
        self.radioButtonStop.setObjectName("radioButtonStop")
        self.frame = QtWidgets.QFrame(KeyActionWidget)
        self.frame.setGeometry(QtCore.QRect(10, 153, 453, 311))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.checkBoxCodeMain = QtWidgets.QCheckBox(self.frame)
        self.checkBoxCodeMain.setGeometry(QtCore.QRect(404, 16, 41, 16))
        self.checkBoxCodeMain.setObjectName("checkBoxCodeMain")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(301, 14, 51, 20))
        self.label_4.setObjectName("label_4")
        self.lineEditRetime = QtWidgets.QLineEdit(self.frame)
        self.lineEditRetime.setGeometry(QtCore.QRect(254, 14, 41, 20))
        self.lineEditRetime.setObjectName("lineEditRetime")
        self.lineEditInterval = QtWidgets.QLineEdit(self.frame)
        self.lineEditInterval.setGeometry(QtCore.QRect(355, 14, 41, 20))
        self.lineEditInterval.setObjectName("lineEditInterval")
        self.plainTextEditCodeMain = QtWidgets.QPlainTextEdit(self.frame)
        self.plainTextEditCodeMain.setGeometry(QtCore.QRect(17, 39, 421, 231))
        self.plainTextEditCodeMain.setObjectName("plainTextEditCodeMain")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 14, 121, 20))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(210, 14, 41, 20))
        self.label_3.setObjectName("label_3")
        self.pushButtonExample = QtWidgets.QPushButton(self.frame)
        self.pushButtonExample.setGeometry(QtCore.QRect(16, 279, 421, 23))
        self.pushButtonExample.setObjectName("pushButtonExample")
        self.frame_2 = QtWidgets.QFrame(KeyActionWidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 83, 453, 61))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.checkBoxCodePre = QtWidgets.QCheckBox(self.frame_2)
        self.checkBoxCodePre.setGeometry(QtCore.QRect(404, 13, 41, 16))
        self.checkBoxCodePre.setObjectName("checkBoxCodePre")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(19, 10, 121, 20))
        self.label_6.setObjectName("label_6")
        self.lineEditCodePre = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditCodePre.setGeometry(QtCore.QRect(19, 33, 421, 25))
        self.lineEditCodePre.setObjectName("lineEditCodePre")

        self.retranslateUi(KeyActionWidget)
        QtCore.QMetaObject.connectSlotsByName(KeyActionWidget)

    def retranslateUi(self, KeyActionWidget):
        _translate = QtCore.QCoreApplication.translate
        KeyActionWidget.setWindowTitle(_translate("KeyActionWidget", "KeyAction"))
        self.label.setText(_translate("KeyActionWidget", "Start"))
        self.label_2.setText(_translate("KeyActionWidget", "Stop"))
        self.pushButtonRun.setText(_translate("KeyActionWidget", "Run"))
        self.labelStatus.setText(_translate("KeyActionWidget", "Status"))
        self.radioButtonExit.setText(_translate("KeyActionWidget", "Exit"))
        self.radioButtonStop.setText(_translate("KeyActionWidget", "Stop"))
        self.checkBoxCodeMain.setText(_translate("KeyActionWidget", "on"))
        self.label_4.setText(_translate("KeyActionWidget", "Interval"))
        self.label_5.setText(_translate("KeyActionWidget", "Main task code"))
        self.label_3.setText(_translate("KeyActionWidget", "Retime"))
        self.pushButtonExample.setText(_translate("KeyActionWidget", "Code Example"))
        self.checkBoxCodePre.setText(_translate("KeyActionWidget", "on"))
        self.label_6.setText(_translate("KeyActionWidget", "Prepare code"))

