# KeyAction--批处理or自动化测试的工具
开发这个工具的原因一开始只是在搞界面原型的时候给表格填写模拟数据时很烦, 就是几个键盘键+鼠标+有规律数据, 然后重复这些动作,
有时候还得重复几十次, 所以就干脆用Python写了键盘+鼠标批处理的脚本, 解放双手...然后为了方便使用不要每次使用都打开工程改代码,
就顺便封装一下开发了该GUI版本;

# 使用说明
1.两个全局快捷键:
* ctrl+alt+shift+F7: 开始执行的动作
* ctrl+alt+shift+F8: 中断执行的动作(stop)或直接退出程序(exit)
* 按下run之后这2个快捷键才开始生效;
<br>
2.两个输入框:
* 输入框都是写python3代码的地方;
* 当按下ctrl+alt+shift+F7时会执行 1次小框的代码 + n次大框的代码;
* 大框一般为主体, 小框一般用来初始化变量;
* 如下图, 当按下ctrl+alt+shift+F7则等价于执行了如下的代码:
self.timemark=10<br>
print(self.timemark)<br>
self.timemark += 2<br>
sleep(0.5)<br>
print(self.timemark)<br>
self.timemark += 2<br>
sleep(0.5)<br>
print(self.timemark)<br>
self.timemark += 2<br>
sleep(0.5)<br>
<img src="https://github.com/shuoGG1239/keyaction/blob/master/readme_img/example1.jpg" alt="example"><br>

# 具体例子
* 在ip这一列填写10个依次递增的ip地址:
* 执行前:
<img src="https://github.com/shuoGG1239/keyaction/blob/master/readme_img/example_axure1.jpg" alt="example">
* 执行后:
<img src="https://github.com/shuoGG1239/keyaction/blob/master/readme_img/example_axure2.jpg" alt="example">

# 可以用的模块
鼠标键盘的操作是用PyUserInput的Api, 直接操作self.keyboard这个对象就行了, <br>
输入框中还可以自己import模块, 像random, os, sys等等都可以;<br>

# 改进
易用性不够, 还要继续改进...

##################################################

# python version
version >= 3

# require the following py modules:
* Pywin32
* PyQt5
* PyUserInput
* PyHook-3k
