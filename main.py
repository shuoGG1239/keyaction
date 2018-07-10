import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
import KeyActionWidget
from QCandyUi import CandyWindow

def run_with_titlebar():
    app = QApplication(sys.argv)
    keywidget = KeyActionWidget.KeyActionWidget()
    mainWindow = CandyWindow.createWindow(keywidget, 'blue')
    mainWindow.setWindowTitle('Key action')
    mainWindow.setWindowIcon(QIcon('myicon.ico'))
    mainWindow.show()
    sys.exit(app.exec_())


def run_only_greentheme():
    app = QApplication(sys.argv)
    mainWindow = KeyActionWidget.KeyActionWidget()
    mainWindow.setWindowIcon(QIcon(window_titlebar.imageroot + 'myicon.ico'))
    green_theme.setAppGreenStyle()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run_with_titlebar()


