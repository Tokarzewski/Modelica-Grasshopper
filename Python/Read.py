from OMPython import OMCSessionZMQ  

omc = OMCSessionZMQ()
omc.sendExpression('loadFile("' + Path +'")')
#print("loadFile(" + ModelPath + '")') #Print Expression

def whatisthat(ClassName):
    options = ['Block','Class','Model','Connector','Constant','Function',
               'Package','Parameter','Primitive','Protected','Record','Type']
    for item in options:
        if omc.sendExpression('is'+item+'('+Name+')') == True:
            answer = item
    return answer

Content = omc.sendExpression('instantiateModel('+ Name +')')
Names = list(omc.sendExpression('getClassNames()'))
Type = whatisthat(Name)