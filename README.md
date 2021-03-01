# -Numerical-control-machine-tool-simulation
Using Python to simulate CNC and other commands

## Overview

> This project was created when I was learning the Turtle, so the root file named "pyturtle" :)

> Please do not change the file name, otherwise, it will destroy the call structure between the files. 

> Please use Windows system, because tkinter is unstable in Linux.

> Please make sure you have all libraries needed.

Run main.py to run the project.

### The libraries you need(based Python 3.7.9, the latest version will work. 2021/2/20):

turtle

tkinter

copy

xml

(just pip these libraries on __Your Windows System__, if you are unix/linux user, don't worry, I'll show you how to simply run this in unix/linux ->[If I am a Linux user, how can I run this?](#1))

### Files need

Please make sure that you have downloaded all of this files(and don't change their relative path):

main.py

operation.py

parameter.py

KeyWords.xml

Funcquired.xml

(other files are not necessary)

<h3 id="1">
If I am a Linux user, how can I run this?
</h3>
 
Frist, open main.py and find these codes in the end of file:

    if __name__ == '__main__':
      Windows()

Second, change them to:

    if __name__ == '__main__':
      m = Main(file, mould, type='CNC')
      m.updata(fs)
      
The parameter "file" is the txt file (.txt) path, "mould" have two choices: "normal" or "step" (what do they mean? I'll talk about later), "type" is command type, like CNC(pre-described) or something else (need custom set up).

And the updata method is to change the scaling multiple of parameters(zoom in or out of the view).

Then, just run and watch :)

## Interface description

When you just run main.py (or create a Windows() object), you will see a simple UI.

In the menu, "模式" is used to switch the command type (default CNC), if you're first time to use it, you'll find another type: "UD", this is a "empty" type, which means it's just a name but nothing will happend before you set it up(so how to set it up? I'll show you later).

Button "选取文件" is to choose txt file to import. And it only support .txt file.

Then you can see the "普通模式" and "单步调试", default module is "normal module". The former means that the animation will play directly, while the latter will play the animation only when you press "Up" Key, and you can press "Down" Key to undo it.

"放大倍数" is to zoom in or zoom out the animation view, it receives any positive number(default is 1).

The biggest entry is just a preview entry, it's readonly.

In the end, press "运行", and just watch!

User definded & API -> pyturtle/descript.md.

# 使用Python的金工命令模拟

## 总览

> 这个项目是我在学习turtle时创建的项目，所以我我决定将这个项目的根目录取为pyturtle。

> 请不要修改该项目所有文件的文件名，否则会破坏文件之间的调用关系。

> 请使用Windows系统，因为tkinter在Linux/unix系统中并不稳定。

> 请确保您已经安装了所以必须的第三方库。

运行main.py来运行这个项目。

### 您需要的第三方库（Python版本3.7.9，截至2021.2.20，所有库版本均为最新即可）：

turtle

tkinter

copy

xml

（只需要简单地用pip在您的Windows上安装即可，对于Linux/Unix用户请看->[如果我是Linux用户，我该怎么办](#2)）

### 文件需要

请确保您已经下载以下所有文件（并请不要改变他们的相对位置）：

main.py

operation.py

parameter.py

KeyWords.xml

Funcquired.xml

（其它的文件并不是必须的）

<h3 id="2">如果我是Linux用户，我该怎么办？</h3>

首先，打开main.py，在文件末尾找到这段代码：

    if __name__ == '__main__':
      Windows()

将其修改成：

    if __name__ == '__main__':
      m = Main(file, mould, type='CNC')
      m.updata(fs)

其中file参数代表需要读取的.txt文件路径，mould参数支持两个值："normal"和"step"（他们的作用我会之后再谈），type参数则是命令种类，默认为CNC（数控车铣）。

updata()方法则可以修改fs，该参数作用是放大或缩小动画视图。

### 界面说明

在菜单栏中的“模式”选项可以选择不同的命令种类（默认为CNC），其中已经设定好了一个用户自定义种类“UD”，只不过它是个“空”的种类，用户必须对它进一步设置才会工作（至于如何自定义，我稍后会讲）。

“选取文件”就是为了选取你要读取的.txt文件。

“普通模式”和“单步调试”则是对应着不同的两种动画模式，默认为普通模式，前者会让动画直接开始播放，一直到结束，后者则只会在用户按下“↑”键的时候才会播放下一步动画，按“↑”则会撤销。

“放缩倍数”接受任何的正数，代表了动画视图放大或缩小的倍数。

最后的空白区域（entry组件）则是一个预览框，用于预览导入的文件，属性为只读。

用户自定义 & API -> pyturtle/descript.md
