import os
import ui_keyactionwidget
import ExampleDialog
from MyPyKeyboardEvent import MyPyKeyboardEvent
import MyPyKeyboardEvent as pykey_module
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot


class KeyActionWidget(QWidget):
    def __init__(self):
        super(KeyActionWidget, self).__init__()
        self.mywidgetui = ui_keyactionwidget.Ui_KeyActionWidget()
        self.keyevent = MyPyKeyboardEvent()
        self.mywidgetui.setupUi(self)
        self.mywidgetui.pushButtonExample.clicked.connect(self.__slot_show_exampledialog)
        self.mywidgetui.pushButtonRun.clicked.connect(self.__slot_runscan)
        self.mywidgetui.pushButtonStop.clicked.connect(self.__slot_stopscan)
        self.mywidgetui.lineEditRetime.textChanged.connect(self.__slot_update_taskargs)
        self.mywidgetui.lineEditInterval.textChanged.connect(self.__slot_update_taskargs)
        self.mywidgetui.plainTextEditCodeStart.textChanged.connect(self.__slot_update_taskstartcode)
        self.__init_innerwidget_status()

    @pyqtSlot(str)
    def __slot_update_taskargs(self, newtext):
        src_obj = self.sender()
        if src_obj.objectName() == 'lineEditRetime':
            self.keyevent.times = int(newtext)
        elif src_obj.objectName() == 'lineEditInterval':
            self.keyevent.interval = float(newtext)

    @pyqtSlot()
    def __slot_update_taskstartcode(self):
        self.keyevent.startcode = self.mywidgetui.plainTextEditCodeStart.toPlainText()

    @pyqtSlot()
    def __slot_show_exampledialog(self):
        ExampleDialog.ExampleDialog().exec()

    @pyqtSlot()
    def __slot_runscan(self):
        if self.mywidgetui.plainTextEditCodeStart.toPlainText() == '':
            self.mywidgetui.labelStatus.setText('Startcode should not be empty!')
            return
        self.mywidgetui.labelStatus.setText('Keyboard Now Listening!!!')
        self.keyevent.set_start_action(self.get_startcode(),self.get_retime(),self.get_interval())
        self.keyevent.set_stop_action(self.get_stopcode())
        self.keyevent.run_all_tasks()

    @pyqtSlot()
    def __slot_stopscan(self):
        pykey_module.stop_startTask()


    def get_checkbox_start_status(self):
        return self.mywidgetui.checkBoxCodeStart.isChecked()

    def get_checkbox_stop_status(self):
        return self.mywidgetui.checkBoxCodeStop.isChecked()

    def get_retime(self):
        return int(self.mywidgetui.lineEditRetime.text())

    def get_interval(self):
        return float(self.mywidgetui.lineEditInterval.text())

    def get_startcode(self):
        return self.mywidgetui.plainTextEditCodeStart.toPlainText()

    def get_stopcode(self):
        return self.mywidgetui.plainTextEditCodeStop.toPlainText()

    def __init_innerwidget_status(self):
        self.mywidgetui.lineEditRetime.setText('3')                     # 执行3次
        self.mywidgetui.lineEditInterval.setText('0.5')                 # 500ms
        self.mywidgetui.lineEditStart.setText('ctrl+alt+shift+F7')
        self.mywidgetui.lineEditStop.setText('ctrl+alt+shift+F8')
        self.mywidgetui.checkBoxCodeStart.setChecked(True)
        self.mywidgetui.checkBoxCodeStop.setChecked(False)
        self.mywidgetui.plainTextEditCodeStart.setPlainText('print("Hello")')
        self.mywidgetui.plainTextEditCodeStop.setPlainText('os._exit(0)')

    def closeEvent(self, e):
        os._exit(0)
