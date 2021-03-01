from pyturtle.operation import *


def N():
    return 'staticAndNone', None

def O():
    return 'staticAndNone', 'Begin'

def M():
    return 'staticAndNone', 'End'

def X():
    return 'static', 'X'

def Y():
    return 'static', 'Y'

def Z():
    return 'staticAndNone', None

'''
以GDZ()为例子，它是G00被读取到时所调用的方法，写法应为
def GDZ():
    return 'moving', function
因为该文件只导入了operation.py，所以只能调用里面的方法，其中包括：
move_to()  对应直线移动命令
circle_l() circle_r() 分别对应画顺圆和逆圆
以上也是目前对应function能够写的内容，前面的'moving'则是一种标记
'''

def GDZ():
    return 'moving', move_to()

"""
可以看到，GDZ和GZO的方法内部是完全一样的，它们的区别是GDZ在调用前会调用pu()，在调用后会调用pd()（体现在xml中）
"""

def GZO():
    return 'moving', move_to()

def GZT():
    return 'moving', circle_l()

def GZH():
    return 'moving', circle_r()

def H():
    return 'staticAndInfo', 'Jinrizhongwuchisha:SHIT'

'''
以GNZ()为例，返回的值依旧是只有两个部分，一部分是用于标记的，固定的'staticAndInfo'，另一部分是一个用:分隔开的字符串。
该字符串的含义就是在视图左下角的信息提示部分，如果当中不包含在“:”前的部分，则会创建这样一行信息，若包含则会更新“:”之后的部分
'''

def GNZ():
    return 'staticAndInfo', 'coordinateMode:Absolute value coordinate mode'

def GFF():
    return 'staticAndNone', 'tooldinateMode:Tool 1'

def GFZ():
    return 'staticAndInfo', 'offsetMode:Cancel offset'

def T():
    return 'staticAndInfo', 'knief:0101'

def GFO():
    return 'staticAndInfo', 'offsetMode:Left offset'


