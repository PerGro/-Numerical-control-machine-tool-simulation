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

