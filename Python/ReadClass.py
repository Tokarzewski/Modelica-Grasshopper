from OMPython import OMCSessionZMQ
from pathlib import Path    

#FileName = Path(FilePath).name.split(".")[0]
ModelPath = ModelPath.replace("\t", "/t")
print(ModelPath)

omc = OMCSessionZMQ()
omc.sendExpression("loadFile(" + '"' + ModelPath +'")')
#Print Expression
print("loadFile(" + '"' + ModelPath +'")')
output_ = omc.sendExpression("instantiateModel("+ClassName+")")