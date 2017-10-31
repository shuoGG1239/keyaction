import os, sys
import ui_keyactionwidget
import ExampleDialog
from MyPyKeyboardEvent import MyPyKeyboardEvent
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject


class KeyActionWidget(QWidget):
    def __init__(self):
        super(KeyActionWidget, self).__init__()
        self.mywidgetui = ui_keyactionwidget.Ui_KeyActionWidget()
        self.keyevent = MyPyKeyboardEvent()
        self.mywidgetui.setupUi(self)
        self.mywidgetui.pushButtonExample.clicked.connect(self.__slot_show_exampledialog)
        self.mywidgetui.pushButtonRun.clicked.connect(self.__slot_runscan)
        self.mywidgetui.lineEditCodePre.textChanged.connect(self.__slot_update_taskargs)
        self.mywidgetui.lineEditRetime.textChanged.connect(self.__slot_update_taskargs)
        self.mywidgetui.lineEditInterval.textChanged.connect(self.__slot_update_taskargs)
        self.mywidgetui.plainTextEditCodeMain.textChanged.connect(self.__slot_update_maintaskcode)
        self.mywidgetui.radioButtonStop.clicked.connect(self.__slot_change_endstyle)
        self.mywidgetui.radioButtonExit.clicked.connect(self.__slot_change_endstyle)
        self.mywidgetui.checkBoxCodeMain.clicked.connect(self.__slot_change_checkbox)
        self.mywidgetui.checkBoxCodePre.clicked.connect(self.__slot_change_checkbox)
        self.__init_innerwidget_status()
        self.__redirect_print()


    @pyqtSlot(str)
    def __slot_update_taskargs(self, newtext):
        src_obj = self.sender()
        if src_obj.objectName() == 'lineEditRetime':
            self.keyevent.times = int(newtext)
        elif src_obj.objectName() == 'lineEditInterval':
            self.keyevent.interval = float(newtext)
        elif src_obj.objectName() == 'lineEditCodePre':
            self.keyevent.precode = newtext

    @pyqtSlot()
    def __slot_update_maintaskcode(self):
        self.keyevent.maincode = self.mywidgetui.plainTextEditCodeMain.toPlainText()

    @pyqtSlot()
    def __slot_show_exampledialog(self):
        ExampleDialog.ExampleDialog().exec()

    @pyqtSlot()
    def __slot_runscan(self):
        if self.mywidgetui.plainTextEditCodeMain.toPlainText() == '':
            self.mywidgetui.labelStatus.setText('Main code should not be empty!')
            return
        self.mywidgetui.pushButtonRun.setEnabled(False)
        self.mywidgetui.labelStatus.setText('Keyboard Now Listening!!!')
        self.keyevent.set_main_action(self.get_maincode(),self.get_retime(),self.get_interval())
        self.keyevent.set_pre_action(self.get_precode())
        self.keyevent.run_all_tasks()

    @pyqtSlot()
    def __slot_change_endstyle(self):
        src_obj = self.sender()
        if src_obj.objectName() == 'radioButtonExit':
            self.keyevent.end_style = 'exit'
        elif src_obj.objectName() == 'radioButtonStop':
            self.keyevent.end_style = 'stop'

    @pyqtSlot()
    def __slot_change_checkbox(self):
        src_obj = self.sender()
        if src_obj.objectName() == 'checkBoxCodeMain':
            self.keyevent.is_main_enable = self.mywidgetui.checkBoxCodeMain.isChecked()
        elif src_obj.objectName() == 'checkBoxCodePre':
            self.keyevent.is_pre_enable = self.mywidgetui.checkBoxCodePre.isChecked()

    def get_checkbox_maincode_sta(self):
        return self.mywidgetui.checkBoxCodeMain.isChecked()

    def get_checkbox_precode_sta(self):
        return self.mywidgetui.checkBoxCodePre.isChecked()

    def get_retime(self):
        return int(self.mywidgetui.lineEditRetime.text())

    def get_interval(self):
        return float(self.mywidgetui.lineEditInterval.text())

    def get_maincode(self):
        return self.mywidgetui.plainTextEditCodeMain.toPlainText()

    def get_precode(self):
        return self.mywidgetui.lineEditCodePre.text()

    def __init_innerwidget_status(self):
        self.mywidgetui.lineEditRetime.setText('3')                     # 执行3次
        self.mywidgetui.lineEditInterval.setText('0.5')                 # 500ms
        self.mywidgetui.lineEditStart.setText('ctrl+alt+shift+F7')
        self.mywidgetui.lineEditStop.setText('ctrl+alt+shift+F8')
        self.mywidgetui.checkBoxCodeMain.setChecked(True)
        self.mywidgetui.checkBoxCodePre.setChecked(True)
        self.mywidgetui.plainTextEditCodeMain.setPlainText('print(self.timemark)')
        self.mywidgetui.lineEditCodePre.setText('self.timemark=10')
        self.mywidgetui.radioButtonExit.click()
        self.mywidgetui.lineEditStart.setReadOnly(True)
        self.mywidgetui.lineEditStop.setReadOnly(True)

    def __redirect_print(self):
        """
        重定向sys.out,使print(text)定向到__refunc(text)
        :return:
        """
        mystream = MyOutStream()
        mystream.textWritten.connect(self.__refunc)
        sys.stdout = mystream

    @pyqtSlot(str)
    def __refunc(self, text):
        useful_text = text.strip()
        if useful_text != '':
            self.mywidgetui.labelStatus.setText(useful_text)

    def closeEvent(self, e):
        sys.stdout = sys.__stdout__     # 归还print输出
        os._exit(0)



# 用于重定向sys.out的类, 只要带write()方法即可
class MyOutStream(QObject):
    textWritten = pyqtSignal(str)
    def write(self, text):
        self.textWritten.emit(str(text))
