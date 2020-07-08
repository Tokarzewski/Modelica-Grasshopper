from OMPython import OMCSessionZMQ  

omc = OMCSessionZMQ()
omc.sendExpression('loadFile("' + ModelPath +'")')
#print("loadFile(" + '"' + ModelPath +'")') #Print Expression
output = omc.sendExpression("instantiateModel("+ClassName+")")