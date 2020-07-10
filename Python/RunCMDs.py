# -*- coding: utf-8 -*-
""" 
Python Script
Created on  Wednesday July 2020 12:06:08 
@author:  amd 

[desc]
Component runs multiple commands
[/desc]

ARGUMENTS:
----------
<inp> 
    cmds :[required] - [type = list] - [default = None] 
    Descripe your input here 
        * first commands
        * seconds commands
</inp>
<inp>
        Run :[required] - [type = bool] - [default = False] 
    Descripe your input here 
        * True to run
        * False to stop
</inp>

RETURN:
----------
    <out>
        output : output from commands
    </out>
"""

#For example
"""cmds = ['loadFile(getInstallationDirectoryPath() + "/share/doc/omc/testmodels/BouncingBall.mo")',
"simulate(BouncingBall)",
"plot(h)"]
Run = True"""

from OMPython import OMCSessionZMQ
if Run == True:
    omc = OMCSessionZMQ()
    output =[]
    for cmd in cmds:
        #change parentheses
        cmd = cmd.replace("[","{").replace("]","}")
        answer = omc.sendExpression(cmd)
        print(cmd)
        output.append("\n{}:\n{}".format(cmd, answer))
else:
    output = "False"