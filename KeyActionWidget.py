import ui_keyactionwidget
import ExampleDialog
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot


class KeyActionWidget(QWidget):
    def __init__(self):
        super(KeyActionWidget, self).__init__()
        self.mywidgetui = ui_keyactionwidget.Ui_KeyActionWidget()
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
        print(self.get_checkbox_start_status())
        print(self.get_checkbox_stop_status())

    @pyqtSlot()
    def __slot_stopscan(self):
        pass

    def get_checkbox_start_status(self):
        return self.mywidgetui.checkBoxCodeStart.isChecked()

    def get_checkbox_stop_status(self):
        return self.mywidgetui.checkBoxCodeStop.isChecked()

    def __init_innerwidget_status(self):
        self.mywidgetui.lineEditRetime.setText('1')                     # 执行1次
        self.mywidgetui.lineEditInterval.setText('0.5')                 # 500ms
        self.mywidgetui.lineEditStart.setText('ctrl+alt+shift+F7')
        self.mywidgetui.lineEditStop.setText('ctrl+alt+shift+F8')
        self.mywidgetui.checkBoxCodeStart.setChecked(True)
        self.mywidgetui.checkBoxCodeStop.setChecked(False)

