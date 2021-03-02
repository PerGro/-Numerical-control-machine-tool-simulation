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

> The methods that can be called in the MovingWords section and their specifications will be mentioned in the [API documents](#1) later. 

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
    
> Actually, for faster running speed, in main.py line 117 and line 141, you can see a list named "nones", and the command included in will be skiped when program detects them. Of cause, you can change them, sacrifice running speed but in exchange for 100% utilization of .xml file. -> [More Information&Operation About This Project]()



<h1 id="1">Project API</h1>
