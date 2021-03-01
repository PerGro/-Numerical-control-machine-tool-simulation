import turtle
import copy
import re
import time
import numpy as np
import xml.dom.minidom
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter.messagebox import showerror
from tkinter.messagebox import showwarning
from pyturtle.operation import *
from pyturtle.parameter import *

LEFT_BUTTON = [-450, -380]
WORD_SIZE = 10


'''
该部分是程序的主要逻辑区，非必要不要做修改
PS:
在turtle中不同文件间对同一个canvas操作时并不会同时记录绘画历史，
但当创建一个新的RawPen时则会被当作为一个操作历史（即使undo也不会让其消失）
'''

class Iter:
    def __init__(self, objects):
        self.point = -1
        self.object = objects
        self.length = len(objects)

    def add(self, item):
        self.object.append(item)
        self.length += 1

    def __check(self):
        if self.point >= self.length or self.point < 0:
            return 0
        return 1

    def next(self):
        self.point += 1
        if self.__check() == 0:
            self.point -= 1
            return 0
        return self.object[self.point]

    def back(self):
        self.point -= 1
        if self.__check() == 0:
            self.point += 1
            return 0
        return self.object[self.point]

    def is_end(self):
        if self.point == self.length - 1:
            return 1
        return 0

    def get(self):
        return self.object[self.point]




'''只能通过Main来调用该类，以确保错误可以显示'''
class Sorter:
    line = None
    line_turtle = None
    def __init__(self, endList, commandList, parametersList, **kwargs):
        '''
        该类负责对接收到的参数进行处理并得出结果
        :param endList: 标志一行结束时词语个数的列表，以0开头
        :param commandList: 只记录命令代码的列表
        :param parametersList: 只记录参数的列表
        :param kwargs: 包括state, fs, type
        '''
        try:
            turtle.home()
        except:
            turtle.home()
        # turtle.reset()
        self.fs = kwargs['fs']
        self.state = kwargs['state']
        self.point = 0
        self.now_point = [0, 0]  # 用于记录当前刀具位置
        self.command_line = 0  # 用于标记指令读取行
        self.dom = xml.dom.minidom.parse('KeyWords.xml')
        self.required = xml.dom.minidom.parse('Funcquired.xml')
        self.func_root = self.required.documentElement
        self.root = self.dom.getElementsByTagName(kwargs['type'])[0]  # 注意这里最后要改成CNC
        self.end_list = endList
        self.command_list = commandList
        self.parameters_list = parametersList
        self.iter = None
        self.parameters_temp = []
        self.infomation_bars = {}
        self.__information_point = []
        self.steps = 0
        self.steps_check = [0]
        self.steps_check_point = 0
        self.now_point_iter = Iter([self.now_point])
        self.__info_init()
        if self.state == 'normal':
            self.__get_normal()
        elif self.state == 'step':
            self.__get_step()

    def __run_step(self):
        global line_turtle, line
        line += 1
        line_turtle.clear()
        line_turtle.write('Now is line ' + str(line))
        turtle.onkeypress(None, 'Up')
        turtle.onkeypress(None, 'Down')
        nones = ['X', 'Y', 'Z', 'O', 'R', 'I', 'J', 'K', 'N', 'M', 'S', 'F', 'D']
        command = self.command_iter.next()
        parameter = self.parameters_iter.next()
        while True:
            if command in nones:
                if self.__check_change_line_steps():
                    command = self.command_iter.next()
                    parameter = self.parameters_iter.next()
                    continue
                else:
                    break
            else:
                self.find_static(command + parameter)
                if self.__check_change_line_steps():
                    command = self.command_iter.next()
                    parameter = self.parameters_iter.next()
                    continue
                else:
                    break
        time.sleep(0.5)
        turtle.onkeypress(self.__run_step, 'Up')
        turtle.onkeypress(self.__undo, 'Down')

    def __get_normal(self):
        nones = ['X', 'Y', 'Z', 'O', 'R', 'I', 'J', 'K', 'N', 'M', 'S', 'F', 'D']
        for index, command in enumerate(self.command_list):
            if command in nones:
                self.__check_change_line()
            else:
                self.find(command + self.parameters_list[index])
                self.__check_change_line()

    def __undo(self):
        global line_turtle, line
        line -= 1
        line_turtle.clear()
        line_turtle.write('Now is line ' + str(line))
        turtle.onkeypress(None, 'Down')
        turtle.onkeypress(None, 'Up')
        turtle.undo()
        if self.command_line == 0:
            return 0
        self.command_line -= 1
        temp = self.point
        self.point = self.end_list[self.command_line] + 1
        while temp != self.point:
            temp -= 1
            self.command_iter.back()
            self.parameters_iter.back()
        self.steps_check_point -= 1
        temp = 0
        while self.steps > self.steps_check[self.steps_check_point]:
            temp += 1
            self.steps -= 1
            turtle.undo()
        self.now_point_iter.back()
        self.steps_check.pop()
        time.sleep(0.5)
        turtle.onkeypress(self.__undo, 'Down')
        turtle.onkeypress(self.__run_step, 'Up')


    def __get_step(self):
        global line_turtle, line
        line = 0
        turtle.listen()
        line_turtle = turtle.RawPen(turtle.getcanvas())
        line_turtle.pu()
        line_turtle.speed(0)
        line_turtle.ht()
        line_turtle.goto(-440, 400)
        line_turtle.write('Now is line 0')
        self.command_iter = Iter(self.command_list)
        self.parameters_iter = Iter(self.parameters_list)
        turtle.onkeypress(self.__undo, 'Down')
        turtle.onkeypress(self.__run_step, 'Up')

    def find_static(self, command_W):
        command_type = self.root.getElementsByTagName(command_W)[0]
        element = copy.deepcopy(command_type)
        command_type = command_type.parentNode.parentNode.nodeName
        if command_type == 'MovingWords':
            self.__picker_s(element)
        elif command_type == 'StaticWords':
            self.__get_attribute_n(element)
        elif command_type == 'Parameter':
            pass
        else:
            ErrorWindow('xml error!')

    def __get_attribute_n(self, element):
        function = element.childNodes[0].data
        ret, func_strings = eval(function + '()')
        func_type, strings = func_strings.split(':')
        type = self.root.getElementsByTagName(func_type)[0].childNodes[0].data
        self.__judge_info(type, strings)

    def __judge_info(self, type, string):
        if self.infomation_bars.get(type) is None:
            self.__create_new_line(type, string)
            self.steps += 1
        else:
            self.__flash(type, string)

    def __picker_s(self, element):
        turtle.seth(0)
        self.steps += 1
        before = element.getAttribute('pereMethod')
        later = element.getAttribute('laterMethod')
        required = int(element.getAttribute('requiredParameters'))
        req = element.getAttribute('required').split(',')
        s = StepsCounter()
        if before != 'None':
            eval('s.' + before + '()')
        main_func = element.childNodes[0].data
        ret, function_ret = eval(main_func + '()')
        function_ret, function = function_ret
        dic = self.__function_open(required, req)
        if len(dic.keys()) < required:
            self.__dic_default(dic)
        dic['last_point'] = list(turtle.pos())
        func_found = self.func_root.getElementsByTagName(function_ret)[0]
        func_para = func_found.getAttribute('required').split(',')
        func_found = func_found.childNodes[0].data
        params = eval('s.' + func_found + '(' + str(dic) + ')')
        params_list = ''
        for para in params:
            params_list = params_list + ',' + str(para)
        params_list = params_list[1:]
        eval('turtle.' + str(function).split(' ')[1] + '(' + params_list + ')')
        self.steps += 1
        turtle.seth(0)
        self.steps += 1
        if later != 'None':
            eval('s.' + later + '()')
        self.now_point = list(turtle.pos())
        # self.steps += s.get()
        self.steps_check.append(self.steps)
        self.steps_check_point += 1

    def __function_reload(self, function=None, parameters=None, updata=None, static=None):
        self.func_dict['function'].append(function)
        self.func_dict['parameters'].append(parameters)
        self.func_dict['updata'].append(updata)
        self.func_dict['static'].append(static)

    def find(self, command_W):
        command_type = self.root.getElementsByTagName(command_W)[0]
        element = copy.deepcopy(command_type)
        command_type = command_type.parentNode.parentNode.nodeName
        if command_type == 'MovingWords':
            self.__picker_m(element)
        elif command_type == 'StaticWords':
            self.__get_attribute_n(element)
        elif command_type == 'Parameter':
            pass
        else:
            ErrorWindow('xml error!')

    def __function_open(self, nums, words):
        point = self.end_list[self.command_line]
        dic = {}
        while point <= self.end_list[self.command_line + 1]:
            for w in words:
                self.command_list[point]
                if w == self.command_list[point]:
                    dic[w] = float(self.parameters_list[point]) * self.fs
            point += 1
        return dic

    def __picker_m(self, element):
        before = element.getAttribute('pereMethod')
        later = element.getAttribute('laterMethod')
        required = int(element.getAttribute('requiredParameters'))
        req = element.getAttribute('required').split(',')
        if before != 'None':
            eval(before + '()')
        main_func = element.childNodes[0].data
        ret, function_ret = eval(main_func + '()')
        function_ret, function = function_ret
        dic = self.__function_open(required, req)
        if len(dic.keys()) < required:
            self.__dic_default(dic)
        dic['last_point'] = self.now_point
        func_found = self.func_root.getElementsByTagName(function_ret)[0]
        # func_para = func_found.getAttribute('required').split(',')
        func_found = func_found.childNodes[0].data
        params = eval(func_found + '(' + str(dic) + ')')
        params_list = ''
        for para in params:
            params_list = params_list + ',' + str(para)
        params_list = params_list[1:]
        eval('turtle.' + str(function).split(' ')[1] + '(' + params_list + ')')
        if later != 'None':
            eval(later + '()')
        if dic.get('X') is not None:
            self.__flash_point(dic['X'], dic['Y'])
        elif dic.get('I') is not None:
            self.__flash_point(dic['I'], dic['J'])

    def __dic_default(self, dic):
        dic.setdefault('X', self.now_point[0])
        dic.setdefault('Y', self.now_point[1])

    def __flash_point(self, x, y):
        self.now_point = [x, y]

    def __check_change_line(self):
        if self.point in self.end_list:
            self.command_line += 1
            # return 1
        self.point += 1
        # return 0

    def __check_change_line_steps(self):
        if self.point in self.end_list:
            self.command_line += 1
            self.point += 1
            return 0
        self.point += 1
        return 1

    def edit_line(self, type, str=None):
        pass

    def __create_new_line(self, type, str=None):
        if len(self.infomation_bars) == 0:
            self.__information_point = LEFT_BUTTON.copy()
        else:
            self.__information_point[1] += WORD_SIZE
        if str is None:
            str = 'None'
        self.infomation_bars[type] = turtle.RawPen(turtle.getcanvas())
        self.infomation_bars[type].ht()
        self.infomation_bars[type].pu()
        self.infomation_bars[type].speed(0)
        self.infomation_bars[type].goto(self.__information_point[0], self.__information_point[1])
        self.infomation_bars[type].write(type + ': ' + str)


    def __flash(self, type, string):
        self.infomation_bars[type].clear()
        self.infomation_bars[type].write(type + ':' + string)

    def __info_init(self):
        init_root = self.func_root.getElementsByTagName('init')[0]
        temp = 0
        for child in init_root.childNodes:
            temp += 1
            if temp % 2 == 0:
                self.__judge_info(child.childNodes[0].data, 'None')
            else:
                continue


class Windows:
    '''
    GUI
    '''
    def __init__(self):
        self.file = None
        self.file_strings = None
        self.scale = 1
        self.dom = xml.dom.minidom.parse('KeyWords.xml')
        self.module = 'normal'
        self.type = None
        self.root = tk.Tk()
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.child_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label='模式', menu=self.child_menu)
        self.root_set()
        self.title_frame()
        self.option_frame()
        self.res_frame()
        self.buttons_frame()
        self.menu_init()
        self.loop()

    def menu_init(self):
        menu_root = self.dom.documentElement
        children = menu_root.childNodes
        index = 0
        for child in children:
            try:
                switch = child.getAttribute('mode')
                if switch == 'On' or switch == 'on':
                    self.child_menu.add_command(label=child.nodeName, command=eval('self.' + child.nodeName))
            except:
                pass
        pass

    '''
    --------------------------------------------------------------------------------
    这里下面的CNC和UD方法都是控制菜单栏中选择模式的
    若要添加，方法名请与xml上节点名称相同
    请不要修改CNC（默认）相关方法，避免出现意外的处理错误
    --------------------------------------------------------------------------------
    '''

    def CNC(self):
        self.type = 'CNC'

    def UD(self):
        self.type = 'UD'

    '''
        --------------------------------------------------------------------------------
        以上的CNC和UD方法都是控制菜单栏中选择模式的
        若要添加，方法名请与xml上节点名称相同
        请不要修改CNC（默认）相关方法，避免出现意外的处理错误（相关请见Windows.__run()中对与默认模式的处理）
        --------------------------------------------------------------------------------
    '''

    def root_set(self):
        self.root.title('金工助手')
        self.root.minsize(width=1280, height=720)
        self.root.maxsize(width=1280, height=720)

    def title_frame(self):
        title_frame = tk.Frame(self.root)
        title_frame.pack(pady=10)
        title_label = tk.Label(title_frame, text='金工助手', font=('黑体', 20, 'bold'))
        title_label.pack(pady=10)

    def option_frame(self):
        option_frame = tk.Frame(self.root)
        option_frame.pack(pady=10)
        self.cs = tk.StringVar()
        self.cs.set('')
        self.choose_entry = tk.Entry(option_frame, width=60, textvariable=self.cs)
        self.choose_entry.grid(row=0, column=0, columnspan=3, padx=10)
        choose_button = tk.Button(option_frame, text='选取文件', command=self.__choose_file)
        choose_button.grid(row=0, column=3, padx=10)
        choose_normal_button = tk.Button(option_frame, text='普通模式', command=self.__choose_normal)
        choose_normal_button.grid(row=1, column=1, padx=20, pady=10)
        choose_step_button = tk.Button(option_frame, text='单步调试', command=self.__choose_step)
        choose_step_button.grid(row=1, column=2, padx=20, pady=10)
        fs_label = tk.Label(option_frame, text='放缩倍数')
        fs_label.grid(row=2, column=1)
        self.fs_int = tk.IntVar()
        self.fs_int.set(self.scale)
        fs_entry = tk.Entry(option_frame, width=10, textvariable=self.fs_int)
        fs_entry.grid(row=2, column=2)

    def res_frame(self):
        res_frame = tk.Frame(self.root)
        res_frame.pack(pady=10)
        self.res_entry = ScrolledText(res_frame, width=150, height=20, undo=True, state=tk.DISABLED)
        self.res_entry.pack(pady=10)

    def buttons_frame(self):
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10)
        run_button = tk.Button(buttons_frame, text='运行', font=('黑体', 20, 'bold'), command=self.__run)
        quit_button = tk.Button(buttons_frame, text='退出', font=('黑体', 20, 'bold'), command=self.__quit)
        run_button.grid(row=0, column=0, padx=20, pady=10)
        quit_button.grid(row=0, column=1, padx=20, pady=10)

    def loop(self):
        self.root.mainloop()

    def __choose_file(self):
        self.file = filedialog.askopenfilename()
        if self.file == '':
            return 0
        if self.file[-3:] != 'txt':
            showwarning('警告！', '本脚本只支持读取txt格式文件（文本文档）')
            return 0
        self.cs.set(self.file)
        self.res_entry.config(state=tk.NORMAL)
        self.res_entry.delete('1.0', tk.END)
        self.file_strings = open(self.file, 'r')
        for line in self.file_strings.readlines():
            self.res_entry.insert(tk.END, line)
        self.res_entry.config(state=tk.DISABLED)
        self.m = Main(self.file, self.module, self.type)
        self.m.check()

    def __choose_normal(self):
        self.module = 'normal'
        showwarning('切换模式成功', '已经切换成一步到位的模式')
        self.m.updata(state=self.module)

    def __choose_step(self):
        self.module = 'step'
        showwarning('切换模式成功', '已经切换成单步调试的模式')
        self.m.updata(state=self.module)

    def __quit(self):
        self.root.destroy()
        self.file_strings.close()

    def __run(self):
        if self.type is None:
            self.type = 'CNC'
        self.m.updata(fs=self.fs_int.get())
        self.m.updata(type=self.type)
        self.m.run()

    def __file(self):
        return self.file


class ErrorWindow:
    '''
    ERROR GUI
    '''
    def __init__(self, errorinfo):
        self.root = tk.Tk()
        self.root_set()
        self.errorinfo = errorinfo
        self.main()
        self.root.mainloop()

    def root_set(self):
        self.root.title('错误！')
        self.root.minsize(width=600, height=400)
        self.root.maxsize(width=600, height=400)

    def main(self):
        error_box = ScrolledText(self.root, width=80, height=40)
        error_box.pack(pady=10, padx=10)
        for line in self.errorinfo:
            error_box.insert(tk.END, line)
        error_box.config(state=tk.DISABLED)

    def quit(self):
        self.root.destroy()


class Main:
    '''
    虽然这个类名与文件名一致，但并不代表此类是类似于main方法一样的主类（笑，其实我也看不懂我在说什么)
    调用Main()时会自动调用__format()与split()，在调用run()后才会实例化一个Sorter对象
    '''
    def __init__(self, file, mould, type):
        if file is None:
            showerror('错误', '还未导入任何文件')
            return 0
        self.fs = 1
        self.root = xml.dom.minidom.parse('KeyWords.xml').getElementsByTagName('Attribute')[0]
        self.func_lib = []
        self.func_lib_len = 0
        self.point_lib = []
        self.start_point = [0, 0]
        self.file = file
        self.state = mould
        self.type = None
        self.file_string = open(self.file, 'r')
        self.file_string_formated = None
        self.infomation = None
        try:
            self.dom = xml.dom.minidom.parse('KeyWords.xml')
        except FileNotFoundError:
            self.dom = None
            showerror('错误', '请检查文件的完整性，缺失文件KeyWords.xml')
        self.__format()
        self.split()

    def updata(self, **kwargs):
        if kwargs.get('fs') is not None:
            self.fs = kwargs['fs']
        elif kwargs.get('state') is not None:
            self.state = kwargs['state']
        elif kwargs.get('type') is not None:
            self.type = kwargs['type']
        elif kwargs.get('file') is not None:
            self.file = kwargs['file']

    def __format(self):
        temp = self.file_string.readlines().copy()
        for index, line in enumerate(temp):
            while line[-2] == ' ':
                temp[index] = temp[index][:-2] + temp[index][-1]
                line = temp[index]
        self.file_string_formated = temp

    def split(self):
        end_counts = [0]
        command_str = []
        command_int = []
        temp_c = 0
        temp = 0
        for line in self.file_string_formated:
            line = line.split(' ')
            for l in line:
                if re.findall(';', l):
                    end_counts.append(temp)
                    temp_c += 1
                command_str.extend(re.findall('[a-zA-Z]+', l)[0])
                command_int.extend(re.findall('-\d+\\.\d+|\d+\\.\d+|-\d+|\d+', l))
                temp += 1
        self.func_lib_len = temp_c
        self.infomation = [end_counts, command_str, command_int]

    def run(self):
        s = Sorter(self.infomation[0], self.infomation[1], self.infomation[2], fs=self.fs, state=self.state, type=self.type)
        # self.__draw()

    # 初始化各类信息(废弃)
    def __draw(self):
        attribute_list = {}
        for child in self.root.childNodes:
            attribute_list[child.data] = turtle.Turtle()
            attribute_list[child.data].pu()
            attribute_list[child.data].ht()
        pass

    def check(self):
        temp = []
        for index, line in enumerate(self.file_string_formated):
            if line[-2] != ';' and line[-1] != ';':
                temp.append('------------------------\n')
                temp.append('前处理错误：句末“;”不完整\n')
                temp.append('在' + str(index + 1) + '行:\n')
                temp.append(line + '\n')
        if len(temp) > 0:
            self.state = 'error'
            e = ErrorWindow(temp)

    def done(self):
        self.file_string.close()

    def __updata(self):
        pass


if __name__ == '__main__':
    Windows()

