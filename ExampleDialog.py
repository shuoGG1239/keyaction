import ui_exampledialog
from  PyQt5.QtWidgets import QDialog

class ExampleDialog(QDialog):
    def __init__(self):
        super(ExampleDialog, self).__init__()
        self.mywidgetui = ui_exampledialog.Ui_ExampleDialog()
        self.mywidgetui.setupUi(self)
        self.mywidgetui.plainTextEditCode.setReadOnly(False)
        self.mywidgetui.plainTextEditCode.setPlainText(self.__getfiletext())

    def __getfiletext(self):
        return open('example.txt','rb').read().decode('utf-8')
