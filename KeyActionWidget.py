import os
import ui_keyactionwidget
import ExampleDialog
from MyPyKeyboardEvent import MyPyKeyboardEvent
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
        self.__init_innerwidget_status()

    @pyqtSlot()
    def __slot_show_exampledialog(self):
        ExampleDialog.ExampleDialog().exec()

    @pyqtSlot()
    def __slot_runscan(self):
        if self.mywidgetui.plainTextEditCodeStart.toPlainText() == '':
            self.mywidgetui.labelStatus.setText('Startcode should not be empty!')
            return
        self.keyevent.set_start_action(self.get_startcode(),5)
        self.keyevent.run_task()

    @pyqtSlot()
    def __slot_stopscan(self):
        print('__slot_stopscan')

    def get_checkbox_start_status(self):
        return self.mywidgetui.checkBoxCodeStart.isChecked()

    def get_checkbox_stop_status(self):
        return self.mywidgetui.checkBoxCodeStop.isChecked()

    def get_startcode(self):
        return self.mywidgetui.plainTextEditCodeStart.toPlainText()

    def __init_innerwidget_status(self):
        self.mywidgetui.lineEditRetime.setText('1')                     # 执行1次
        self.mywidgetui.lineEditInterval.setText('0.5')                 # 500ms
        self.mywidgetui.lineEditStart.setText('ctrl+alt+shift+F7')
        self.mywidgetui.lineEditStop.setText('ctrl+alt+shift+F8')
        self.mywidgetui.checkBoxCodeStart.setChecked(True)
        self.mywidgetui.checkBoxCodeStop.setChecked(False)

    def closeEvent(self, e):
        os._exit(0)
