import KeyActionWidget
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = KeyActionWidget.KeyActionWidget()
    mainWindow.show()
    sys.exit(app.exec_())