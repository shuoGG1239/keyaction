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

end_circle = False
def stop_mainTask():
    """
    结束掉dotimes的循环
    :return: void
    """
    global end_circle
    end_circle = True


# 这里结束线程方法只作为示范,没有实际用到该项目
end_thread = False
def stop_mainThread():
    """
    py的Thread没有stop方法, 须用标志位方式来自然结束线程
    :return: void
    """
    global end_thread
    end_thread = True


# @装饰器start
def on_startbuttons_clicked(func):
    def startwork(*args, **kwargs):
        global isStart, end_thread
        while True:
            if isStart:
                print('-------------------start------------------')
                isStart = False
                func(*args, **kwargs)
            time.sleep(0.01)
            if end_thread:    # True时,结束该循环,线程threadstart自然死去
                end_thread = False
                break
        print("start thread is dead")
    return startwork

# @装饰器stop
def on_stoptbuttons_clicked(func):
    def exitwork(*args, **kwargs):
        global isEnd
        while True:
            if isEnd:
                print('-------------------end------------------')
                isEnd = False
                func(*args, **kwargs)
            time.sleep(0.01)
    return exitwork


class MyPyKeyboardEvent(PyKeyboardEvent):
    def __init__(self):
        PyKeyboardEvent.__init__(self)
        self.times = 1
        self.interval = 0.5
        self.maincode = str('print("start!!!")')
        self.precode = str('self.timemark=10')
        self.timemark = 1
        self.end_style = 'exit'     # ENUM: exit stop
        self.is_pre_enable = True
        self.is_main_enable = True

        self.keyboard = PyKeyboard()
        self.isF7Press = False
        self.isF8Press = False
        self.isLeftctrlPress = False
        self.isLeftaltPress = False
        self.isLeftshiftPress = False

    def set_main_action(self, maincode, times=1, interval=0.5):
        self.maincode = maincode
        self.times = times
        self.interval = interval

    def set_pre_action(self, precode):
        self.precode = precode

    def run_all_tasks(self):
        self.threadstart = Thread(target=self.service)
        self.threadstop = Thread(target=self.exit_system)
        self.threadkey = Thread(target=self.run)
        self.threadstart.start()
        self.threadstop.start()
        self.threadkey.start()
        print('KeyBoard task is running now!!!')

    def run_start_task(self):
        self.threadstart = Thread(target=self.service)
        self.threadstart.start()

    def tap(self, keycode, character, press):
        global isStart,isEnd
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
            isStart = True

        # ctrl+alt+shift+F8
        if self.isF8Press == True and self.isLeftctrlPress == True and self.isLeftaltPress == True and self.isLeftshiftPress == True:
            isEnd = True

    def main_do(self):
        try:
            exec(self.maincode)
        except Exception as e:
            print(e)

    def pre_do(self):
        try:
            exec(self.precode)
        except Exception as e:
            print(e)

    @on_startbuttons_clicked
    def service(self):
        if self.is_pre_enable:
            self.pre_do()
        if self.is_main_enable:
            self.dotimes(self.main_do, self.times, self.interval)

    @on_stoptbuttons_clicked
    def exit_system(self):
        if self.end_style == 'exit':
            os._exit(0)
        elif self.end_style == 'stop':
            stop_mainTask()

    # 以intervals时间间隔干times次func
    def dotimes(self, func, times, interval):
        if times <= 0 or interval < 0:
            return
        global end_circle
        for x in range(0, times):
            if interval != 0:
                time.sleep(interval)
            func()
            if end_circle:
                end_circle = False
                break

