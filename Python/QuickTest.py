import OMPython, modelica_language, modelicalang, pymoca, pyfmu, buildingspy, impactlib

from OMPython import OMCSessionZMQ
output = []
omc = OMCSessionZMQ()
output.append(omc.sendExpression("getVersion()"))
output.append(omc.sendExpression("loadModel(Modelica)"))
output.append(omc.sendExpression("loadFile(getInstallationDirectoryPath() + \"/share/doc/omc/testmodels/BouncingBall.mo\")"))
output.append(omc.sendExpression("instantiateModel(BouncingBall)"))
output.append(omc.sendExpression("simulate(BouncingBall, stopTime=3.0)"))
omc.sendExpression("val(h , 2.0)")

output_ = '\n'.join(map(str, output))