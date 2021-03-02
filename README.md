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

# 以下内容也可以在pyturtle/descript.md中查阅

# User Definded

When you want to add new command or even add new command type, you will need them:

## KeyWords.xml

In this file, you can see that under the root node, there are different command type nodes:

    <KeyWords>
      <CNC>
        ......
      </CNC>
      
      <UD>
      </UD>

In command type nodes (ex. CNC), they all have four fixed part:

    <CNC>
      <MovingWords>
        ......
      </MovingWords>
      
      <StaticWords>
        ......
      </StaticWords>
      
      <Parameters>
        ......
      </Parameters>
      
      <Attribute>
        ......
      </Attribute>
    </CNC>
    
They are *MovingWords*, *StaticWords*, *Parameters*, *Attribute*. Now let me show you that how to work with them.

### MovingWords: Used to mark the commands that will make the knief or tool move

For this node, its child nodes should have same structure like:

    <MovingWords>
    <!-- node G 's child nodes should be like GXX -->
      <G>
        <G00 pereMethod="pu" laterMethod="pd" requiredParameters='2' required="X,Y">GDZ</G00>
        <!-- something just like node G00 -->
      </G>
    </MovingWords>
    
In node G00, we can see it have several attributes, the "pereMethod" means when this command (G00) is detected, before calling the method it have, it will calling the method which is stored in "pereMethod". For example, if I have a method named f, and I hope when the G200 command is detected, it will call f first (Suppose that the original corresponding command of G200 is "move"), we can add a node like this:

    <MovingWords>
    <!-- node G 's child nodes should be like GXX -->
      <G>
        <G00 pereMethod="pu" laterMethod="pd" requiredParameters='2' required="X,Y">GDZ</G00>
        <!-- something just like node G00 -->
        <!-- add G200 -->
        <G200 pereMethod="f" laterMethod="None" requiredParameters='1' required="X">move</G200>
      </G>
    </MovingWords>
    
> Shoule be attention to: whatever pereMethod or laterMethod attribute, they can only call method without parameter in parameter.py or operation.py.

laterMethod is just like the pereMethod, but the method it points to is called only after calling the node's method.

> Tips: you should write "None" when you don't want anything happend.

> Maybe you think these two attributes is useless, but if you choose single step debugging module (remember that?), it will show its magic power. 

requiredParameter attribute means the minimum parameters required for command.

For example, command G02 have two situation:

    G02 I20 J20;

or

    G02 X20 Y20 R40;
    
In the first case, G02 need two parameters: I20 J20. But in the second case, G02 need three parameters: X20 Y20 R40. But attribute "requiredParameter" need the least parameter number, so if I want to add G02 command to KeyWords.xml, I'll do like:

    <MovingWords>
    <!-- node G 's child nodes should be like GXX -->
      <G>
        <G00 pereMethod="pu" laterMethod="pd" requiredParameters='2' required="X,Y">GDZ</G00>
        <!-- something just like node G00 -->
        <!-- add G200 -->
        <G200 pereMethod="f" laterMethod="None" requiredParameters='1' required="X">move</G200>
        <!-- add G02 -->
        <G02 pereMethod="None" laterMethod="None" requiredParameters='2' required="X,Y,I,J,K">some_function</G02>
      </G>
    </MovingWords>

You'll find the required attribute need the all of parameters' command, and please separate with commas only.

Finally, if you want to bind a method to a command, just add method to command's node.

    <MovingWords>
    <!-- node G 's child nodes should be like GXX -->
      <G>
        <G00 pereMethod="pu" laterMethod="pd" requiredParameters='2' required="X,Y">GDZ</G00>
        <!-- something just like node G00 -->
        <!-- add G200 -->
        <G200 pereMethod="f" laterMethod="None" requiredParameters='1' required="X">move</G200>
        <!-- add G02 -->
        <!-- we want to add method circle_l to G02, just put it in -->
        <G02 pereMethod="None" laterMethod="None" requiredParameters='2' required="X,Y,I,J,K">circle_l</G02>
      </G>
    </MovingWords>

> More command templates in KeyWords.xml

> The methods that can be called in the MovingWords section and their specifications will be mentioned in the [API documents](#3) later. 

### StaticWords: Used to mark the command that does not move the tool, but alse includes the command to updata the current information.

Its structure is same like MovingWords:

    <StaticWords>
      <G>
        <G40>GFZ</G40>
        <!-- some other Gxx command -->
      </G>
      
      <N>
        <N>N</N>
      </N>
    </StaticWords>
    
> Actually, for faster running speed, in main.py line 117 and line 141, you can see a list named "nones", and the command included in will be skiped when program detects them. Of cause, you can change them, sacrifice running speed but in exchange for 100% utilization of .xml file. -> [More Information&Operation About This Project.]()

Compared with former section, StaticWords's node don't have any attribute (Although this may not be the case in the file, but any attributes in this section do not work).

In this case, the methods called will flash the animation information (in the lower left conrner of animation view), know more -> [API documents](#3).

### Parameter: Used to mark coordinate command

This section is so simple ... it just store just like X Y Z I J K R commands...

> In a word, it is responsible for managing the commands that need to provide parameters for the MovingWords' commands.

### Attribute: Used to mark animation information

In this case, all of nodes fllow the rules:

    <Attribute>
      <information_funcition_name>information_display</information_function_name>
    </Attribute>
    
Let's take an example, in these codes:

    <Attribute>
      <coordinateMode>Coordinate Mode</coordinateMode>
    </Attribute>
    
and in parameter.py, we have a method:

    def GNZ():
        return 'staticAndInfo', 'coordinateMode:Absolute value coordinate mode'

this method will be called when program detects the 'G90' command, and it just return two parameters, 'staticAndInfo' just a mark (but it's necessary), 'coordinateMode:Absolute value coordinate mode' will talk to program: "Hey! We need find coordinateMode section and change its content to 'Absolute value coordinate mode'!"

and when your program detects 'G90' command, on lower left corner, will write a line:
    
    Coordinate Mode: Absolute value coor
    
## Funcquired.xml

In this file, for every different command type nodes, they only have two parts: init part & function contect part.

    <Functions>
      <CNC>
        <!-- init part -->
        <init>
          <coordinateMode>Coordinate Mode</coordinateMode>
        </init>
        
        <!-- function contect part -->
        <circle_l>clockwise_circle</circle_l>
      </CNC>
    </Functions>
    
The information are stored in init nodes (they need same format just like they in KeyWords.xml) will write to the lower left corner on canvas before beginning.

And the purpose of other nodes is to explain that in order to execute the method named by node name, the method within the node must be called because of the need of parameters.(all of this method should be wrote in operation.py)

Take the above code as an example:

    <circle_l>clockwise_circle</circle_l>
    
this line means when program need call operation.circle_l(), it need parameters from operation.clockwise_circle().

> Every method that try to move the point should contect with another method to get enough parameters.

<h1 id="3">Project API</h1>

Let's start easy though:

## main.py

### main.Windows(): GUI class

### main.Main(): Class for pretreatment

Main.split(): used to separate command strings from numbers, and store them as different list (self.).

Main.run(): used to create a Sorter() object, which is contrl animation.

Main.check(): used to preprocessing text. If program meet error, it will create ErrorWindow() object and output.

## parameter.py

__*Overview*__: 

Every method in this file just need return two parts. First is a kind of mark, you can choose one of them: 'staticAndNone', 'static', 'moving', 'staticAndInfo'. The second is importent, if this method is contect with a moving command, the second return should be a method, if this method do nothing, it should be None, if this method will change animation information, it should be a string list.

For moving command, operation.py provides three public method: move_to() for straight line movement, circle_l() for clockwise rotation, circle_r() for anti-clockwise rotation.

## operation.py

operation.clockwise_circle(kwargs): used to provide parameters for the clockwise circle drawing method, it will return two parameters, one is radius, another is theta. Radius means the circle's radius, theta means turtle's orientation.

When it works with turtle.circle(), it will find suitable path to draw a clockwise arc to contact the point A (input) and the point B (destination).

> The major are is drawn only when the R value in the incoming parameter is negative.

operation.anti_clockwise_circle(kwargs): just like operation.clockwise_circle(kwargs), when it works with turtle.circle(), it will fin suitable path to draw a anti-clockwise arc to contact the point A (input) and the point B (destination).

> The major are is drawn only when the R value in the incoming parameter is negative.

operation.move_to_temp(): just return the parameters to work with turtle.goto().
