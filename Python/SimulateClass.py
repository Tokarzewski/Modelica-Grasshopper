from OMPython import OMCSessionZMQ
omc = OMCSessionZMQ()

#ModelPath=omc.sendExpression("getInstallationDirectoryPath()") + "/share/doc/omc/testmodels/" + "BouncingBall.mo"
from OMPython import ModelicaSystem
mod=ModelicaSystem(ModelPath,ClassName)
#3 arguments #mod=ModelicaSystem(ModelPath, ClassName, ["Modelica"])
#4 arguments #mod=ModelicaSystem(ModelPath, ClassName, commandLineOptions="-d=newInst")
Quantities = mod.getQuantities()
SimOptions = mod.getSimulationOptions()

if RunSimulation == True:
    mod.simulate()
    Solutions = list(mod.getSolutions())
else:
    Solutions = mod.getSolutions()