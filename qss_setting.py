from PyQt5.QtWidgets import QSlider, QLineEdit, QPushButton, QProgressBar

# global css to use
qss = ""

# const color string
WHITE = "#FFFFFF"
BLACK = "#000000"
RED = "#FF0000"
GREEN = "#00FF00"
BLUE = "#0000FF"
PURPLE = "#B23AEE"
WATCHET = "#1C86EE"
LIGHTGREEN = "#ECFEFE"
BLUEGREEN = "#33CCCC"
DEEPBLUEGREEN = "#015F5F"
DARKBLUEGREEN = "#28AAAA"
GRAY = "#999999"
LIGHTGRAY = "#CCCCCC"


def getFontQss(fontname, fontcolor):
    return "QObject{font-family:%s;color:%s}" % (fontname, fontcolor)


def getPushButtonQss(normalColor, normalTextColor, hoverColor, hoverTextColor, pressedColor, pressedTextColor,
                     disableColor, disableTextColor):
    str1 = "QPushButton{padding:0px;border-radius:5px;color:%s;background:%s;border:2px solid %s;}" % (
    normalTextColor, normalColor, normalColor)
    str2 = "QPushButton:hover{color:%s;background:%s;}" % (hoverTextColor, hoverColor)
    str3 = "QPushButton:pressed{color:%s;background:%s;" % (pressedTextColor, pressedColor)
    str4 = "QPushButton:disabled{color:%1;background:%2;}" % (disableTextColor, disableColor)
    return str1 + str2 + str3 + str4


def getLineeditQss(normalColor, focusColor):
    pass


def getPlaineditQss(normalColor, focusColor):
    pass


def getComboxQss(backgroundColor, normalColor, focusColor, arrowimageurl):
    pass


def getProgressBarQss(normalColor, chunkColor):
    pass


def getSliderQss(normalColor, grooveColor, handleColor):
    pass


def getRadioButtonQss(normimageurl, downimageurl, normimageurlhover, downimageurlhover):
    pass


def getCheckBoxQss(normimageurl, checkimageurl, normimageurlhover, checkimageurlhover):
    pass


def getTabWidgetQss(normalTabColor, normalTabTextColor):
    pass


def getScrollbarQss(handlebarcolor):
    pass


def clearQssStr():
    pass
