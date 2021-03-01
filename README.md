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

In the menu, "模式" is used to switch the command type (default CNC), if you're first time to use it, you'll find another type: "UD", this is a "empty" type, which means it's just a name but nothing will happend before you set it up.

Button "选取文件" is to choose txt file to import. And it only support .txt file.

Then you can see the "普通模式" and "单步调试", default module is "normal module". The former means that the animation will play directly, while the latter will play the animation only when you press "Up" Key, and you can press "Down" Key to undo it.

"放大倍数" is to zoom in or zoom out the animation view, it receives any positive number(default is 1).

The biggest entry is just a preview entry, it's readonly.

In the end, press "运行", and just watch!
