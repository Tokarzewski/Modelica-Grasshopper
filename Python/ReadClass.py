from OMPython import OMCSessionZMQ  

omc = OMCSessionZMQ()
omc.sendExpression('loadFile("' + ModelPath + '")')
#print("loadFile(" + ModelPath + '")') #Print Expression

ClassContent = omc.sendExpression("instantiateModel("+ ClassName +")")
ClassNames = list(omc.sendExpression("getClassNames()"))