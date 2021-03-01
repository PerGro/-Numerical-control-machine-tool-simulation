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

# Project API
