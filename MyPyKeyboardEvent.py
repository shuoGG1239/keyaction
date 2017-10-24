from pykeyboard import PyKeyboardEvent
from pykeyboard import PyKeyboard
from threading import Thread
import time
import os

'''
    ctrl+alt+shift+F7--->开始
    ctrl+alt+shift+F8--->结束
    想干的事用@on_startbuttons_clicked修饰
'''

isStart = False
isEnd = False


class MyPyKeyboardEvent(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.isF7Press = False
        self.isF8Press = False
        self.isLeftctrlPress = False
        self.isLeftaltPress = False
        self.isLeftshiftPress = False

    def tap(self, keycode, character, press):
        # print(keycode, character, press)
        if character == 'LCONTROL':
            if press == True:
                self.isLeftctrlPress = True
            else:
                self.isLeftctrlPress = False

        if character == 'LMENU':
            if press == True:
                self.isLeftaltPress = True
            else:
                self.isLeftaltPress = False

        if character == 'LSHIFT':
            if press == True:
                self.isLeftshiftPress = True
            else:
                self.isLeftshiftPress = False

        if character == 'F8':
            if press == True:
                self.isF8Press = True
            else:
                self.isF8Press = False

        if character == 'F7':
            if press == True:
                self.isF7Press = True
            else:
                self.isF7Press = False

        # ctrl+alt+shift+F7
        if self.isF7Press == True and self.isLeftctrlPress == True and self.isLeftaltPress == True and self.isLeftshiftPress == True:
            global isStart
            isStart = True

        # ctrl+alt+shift+F8
        if self.isF8Press == True and self.isLeftctrlPress == True and self.isLeftaltPress == True and self.isLeftshiftPress == True:
            global isEnd
            isEnd = True


# area_num = 100001
# area_num = 65
area_num = 1
def doRename():
    global keyBoard
    global area_num
    # keyBoard.tap_key(keyBoard.function_keys[2])      # F2
    # keyBoard.type_string('data_auto20160606200'+str(area_num)+'.bak') 
    # keyBoard.type_string(str(round(random.uniform(20,40),2)))
    # keyBoard.type_string('WM'+str(area_num))
    # keyBoard.type_string(chr(area_num))
    keyBoard.type_string('192.168.75.'+str(area_num))
    keyBoard.tap_key(keyBoard.down_key)                # 方向键下
    area_num += 1

myasciiA = ord('A') 
def doRename_A():
    global keyBoard
    global myasciiA
    # keyBoard.tap_key(keyBoard.function_keys[2])      # F2
    keyBoard.type_string('area'+chr(myasciiA))         # type a string
    keyBoard.tap_key(keyBoard.down_key)                # 方向键下
    myasciiA += 1


# 以intervals时间间隔干times次func
def dotimes(func, times, intervals):
    for x in range(0, times):
        if intervals != 0:
            time.sleep(intervals)
        func()

# @装饰器1
def on_startbuttons_clicked(func):
    def startwork(*args, **kwargs):
        global isStart
        while True:
            if isStart:
                print('-------------------start------------------')
                isStart = False
                func(*args, **kwargs)
            time.sleep(0.01)
    return startwork

# @装饰器2
def on_endbuttons_clicked(func):
    def exitwork(*args, **kwargs):
        global isEnd
        while True:
            if isEnd:
                print('-------------------end------------------')
                func(*args, **kwargs)
            time.sleep(0.01)
    return exitwork


@on_endbuttons_clicked
def exit_system():
    os._exit(0)

@on_startbuttons_clicked
def opt_axure():
    # dotimes(doRename, 15, 0.5)
    global aop_code
    exec(aop_code)

aop_code = str()
def dohello():
    print('hello')


if __name__=='__main__':
    print('================System on=================')
    aop_code = 'dotimes(dohello, 10, 0.5)'
    keyBoard = PyKeyboard()
    thread1 = Thread(target=opt_axure)
    thread1.start()
    thread2 = Thread(target=exit_system)
    thread2.start()
    p = MyPyKeyboardEvent()
    p.run()

    # exec(code)                # 实现aop,实现各种酷炫动态修改,直接影响runtime
    # execfile('abc.py')        # 在py里运行另外一个py
    # os.system('abc.py 123')   # 在py里运行另外一个py,带参数
    # os.popen('abc.py 123')    # 和os.system很相似,只是返回是file,相当于管道,返回来执行完的输出结果